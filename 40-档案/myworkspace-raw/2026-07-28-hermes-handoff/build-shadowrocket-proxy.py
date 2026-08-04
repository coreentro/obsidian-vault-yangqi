#!/usr/bin/env python3
"""Build a temporary sing-box proxy from one Shadowrocket VLESS node.

Secrets are read directly from Shadowrocket's protected archive and written
only to an owner-readable output file. They are never printed or accepted as
command-line arguments.
"""

from __future__ import annotations

import argparse
import json
import os
import plistlib
from pathlib import Path


DEFAULT_ARCHIVE = Path(
    "/Users/yangqi/Library/Group Containers/"
    "group.com.liguangming.Shadowrocket/ServerManager"
)


def resolve(objects: list, value):
    while isinstance(value, plistlib.UID):
        value = objects[value.data]
    if isinstance(value, dict) and "NS.string" in value:
        return resolve(objects, value["NS.string"])
    return value


def find_node(objects: list, title: str) -> dict:
    for item in objects:
        if not isinstance(item, dict) or "title" not in item:
            continue
        if resolve(objects, item["title"]) == title:
            return item
    raise ValueError(f"Shadowrocket node not found: {title}")


def node_value(objects: list, node: dict, key: str, default=None):
    if key not in node:
        return default
    return resolve(objects, node[key])


def build_config(
    objects: list,
    node: dict,
    server_ip: str,
    listen_port: int,
    log_level: str,
) -> dict:
    node_type = str(node_value(objects, node, "type", "")).lower()
    if node_type != "vless":
        raise ValueError(f"only VLESS is supported, got {node_type!r}")

    # Shadowrocket's archived `uuid` is the row identifier. For VLESS, the
    # protocol credential is stored in `password` (subscription siblings share
    # it while each row has a different `uuid`).
    uuid = str(node_value(objects, node, "password", ""))
    public_key = str(node_value(objects, node, "publicKey", ""))
    short_id = str(node_value(objects, node, "shortId", ""))
    server_name = str(node_value(objects, node, "peer", ""))
    server_port = int(node_value(objects, node, "port", 0))
    if not all((uuid, public_key, server_name, server_port)):
        raise ValueError("selected node is missing required VLESS Reality fields")

    return {
        "log": {"level": log_level, "timestamp": True},
        "inbounds": [
            {
                "type": "mixed",
                "tag": "oauth-in",
                "listen": "127.0.0.1",
                "listen_port": listen_port,
            }
        ],
        "outbounds": [
            {
                "type": "vless",
                "tag": "oauth-out",
                "server": server_ip,
                "server_port": server_port,
                "uuid": uuid,
                "flow": "xtls-rprx-vision",
                "tls": {
                    "enabled": True,
                    "server_name": server_name,
                    "insecure": bool(
                        node_value(objects, node, "allowInsecure", False)
                    ),
                    "utls": {"enabled": True, "fingerprint": "chrome"},
                    "reality": {
                        "enabled": True,
                        "public_key": public_key,
                        "short_id": short_id,
                    },
                },
            }
        ],
        "route": {"final": "oauth-out"},
    }


def secure_write(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor = os.open(
        path,
        os.O_WRONLY | os.O_CREAT | os.O_TRUNC,
        0o600,
    )
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            json.dump(payload, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
    finally:
        os.chmod(path, 0o600)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--title", required=True)
    parser.add_argument("--server-ip", required=True)
    parser.add_argument("--listen-port", type=int, default=18082)
    parser.add_argument(
        "--log-level",
        choices=("trace", "debug", "info", "warn", "error"),
        default="warn",
    )
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--archive", type=Path, default=DEFAULT_ARCHIVE)
    args = parser.parse_args()

    archive = plistlib.loads(args.archive.read_bytes())
    objects = archive.get("$objects", [])
    node = find_node(objects, args.title)
    config = build_config(
        objects,
        node,
        args.server_ip,
        args.listen_port,
        args.log_level,
    )
    secure_write(args.output, config)
    print(
        json.dumps(
            {
                "output": str(args.output),
                "mode": oct(args.output.stat().st_mode & 0o777),
                "listen": f"127.0.0.1:{args.listen_port}",
                "node_type": "vless-reality",
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
