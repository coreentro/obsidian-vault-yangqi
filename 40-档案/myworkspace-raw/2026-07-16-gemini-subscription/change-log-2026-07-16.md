# Gemini subscription change log

Date: 2026-07-16

## Changes

1. Installed and investigated the official CPA Gemini CLI plugin.
2. Completed Google OAuth and age verification for `yangqihello@gmail.com`.
3. Confirmed Google recognizes the account as `Gemini Code Assist in Google One AI Pro`.
4. Identified the upstream migration notice: Gemini CLI no longer serves Google One and unpaid tiers after 2026-06-18.
5. Completed Antigravity OAuth for the same account and saved the native CPA credential.
6. Disabled the obsolete `gemini-cli` plugin route to avoid 429 responses and model collisions.
7. Kept CPA's proxy at `http://127.0.0.1:7897` and restored `debug` and `logging-to-file` to `false`.
8. Linked Google Cloud project `project-c785eaec-3265-4f46-8ba` (`My First Project`) to billing account `01853F-026EED-D4DDE1`, which is administered by `entrocore@gmail.com`.
9. Enabled `aiplatform.googleapis.com` on the project.
10. Granted `yangqihello@gmail.com` the project-level `Agent Platform User` role without granting billing-management permissions.
11. Reauthenticated the Antigravity desktop app as `yangqihello@gmail.com` and configured it to use `project-c785eaec-3265-4f46-8ba` in the `global` location.
12. Created billing-account budget `antigravity-monthly-0-1-usd` on `01853F-026EED-D4DDE1`: monthly budget US$0.10, actual-spend alerts at US$0.05, US$0.09, and US$0.10.
13. Lowered the `gemini-3.5-flash-cyber` quota `Global generate content requests per minute per project per base model` from 250 to 10 requests/minute.
14. Reverted that manual quota override: the `gemini-3.5-flash-cyber` quota is back to the default 250 requests/minute.
15. Attempted to switch Antigravity back to the Google AI Pro sign-in route using `yangqihello@gmail.com`; Antigravity reported that this account is currently ineligible, so the Cloud fallback was left intact rather than making the app unusable.
16. Tested the same Google sign-in flow with `entrocore@gmail.com`; Google OAuth succeeded, but Antigravity returned the same ineligible-account error.
17. Tested `liliyoungqi@gmail.com` as another personal Google account; Google OAuth completed, but Antigravity again returned the same ineligible-account error.
18. Found an active native Antigravity OAuth credential for `yangqihello@gmail.com` under CPA/CLIProxyAPI; this third-party route was disabled reversibly by moving it to a timestamped `.disabled-*` backup, then the CPA service was restarted.
19. Retried the official Antigravity desktop OAuth flow after disabling the third-party credential. Google OAuth completed, the initial setup timeout was cleared by restarting Antigravity, and the desktop app returned to its normal workspace.
20. Per user request, restored the CPA Antigravity credential from its reversible backup and restarted the CPA service.
21. Explicitly selected `yangqihello@gmail.com` in the official Google OAuth chooser and confirmed the account identity on Google's warning page.
22. Clicked the final Google “Login” authorization button; OAuth returned to Antigravity, which again reported “This account is ineligible to use Antigravity”.
23. Removed `yangqihello@gmail.com` from project `project-c785eaec-3265-4f46-8ba` in Google Cloud by revoking its `roles/aiplatform.user` IAM binding; billing ownership remains with `entrocore@gmail.com`.
24. Diagnosed Hermes' endless retries: the current session requested `gemini-3.1-pro-preview`, but CPA exposes `gemini-3.1-pro-low` and does not expose the preview ID; CPA itself had also been stopped.
25. Started CPA, verified the supported model and a real completion, switched the Hermes session to `gemini-3.1-pro-low`, removed the stale preview model from Hermes' curated custom-provider list, and restarted Hermes.

## Verification

- CPA service: running on `127.0.0.1:8317`.
- Auth provider: `antigravity`.
- Account: `yangqihello@gmail.com`.
- Models endpoint: HTTP 200; Antigravity Gemini models are present.
- Chat completion: `gemini-3-flash`, HTTP 200, response `收到`.
- Project billing: enabled through billing account `01853F-026EED-D4DDE1`.
- Agent Platform API: enabled on `project-c785eaec-3265-4f46-8ba`.
- IAM: `yangqihello@gmail.com` is listed as `Agent Platform User` on the project.
- Antigravity desktop app: account settings show `yangqihello@gmail.com`; current model is `Gemini 3.5 Flash (Medium)`.
- Antigravity live test: the prompt `test` completed successfully with the response `Hello! I am ready to help you with your coding tasks. How can I assist you today?`.
- Billing budget: `antigravity-monthly-0-1-usd` is listed on billing account `01853F-026EED-D4DDE1` at US$0.10/month with 50%/90%/100% thresholds.
- Quota: the Google Cloud quota page confirms `gemini-3.5-flash-cyber` is restored to the default 250 requests/minute.
- Antigravity subscription route: `yangqihello@gmail.com` currently returns “Sorry, this account is ineligible to use Antigravity”.
- A second personal account, `entrocore@gmail.com`, produced the same Antigravity eligibility error after successful Google OAuth.
- A third personal account, `liliyoungqi@gmail.com`, produced the same error as well.
- After disabling the active CPA Antigravity credential and restarting the desktop app, Antigravity loaded its normal workspace; the language-server log records `Auth succeeded` and `initialized server successfully`.
- The CPA credential was not deleted; it was moved to `/Users/yangqi/.cli-proxy-api/antigravity-yangqihello@gmail.com.json.disabled-20260716-204751` for reversible rollback.
- Per user request, the credential is restored at `/Users/yangqi/.cli-proxy-api/antigravity-yangqihello@gmail.com.json`; CPA is running again.
- Latest official OAuth test: Google accepted the selected account, but Antigravity's post-login eligibility check rejected it.
- Google Cloud IAM verification: `yangqihello@gmail.com` is no longer a member of `project-c785eaec-3265-4f46-8ba`.
- Hermes verification: the repaired session returned `OK` through `gemini-3.1-pro-low`; CPA is loaded and listening on `127.0.0.1:8317`.
- A backup of the Hermes session database was created at `/Users/yangqi/.hermes/state.db.bak-before-gemini-low-20260716-215746` before changing the session model.

No OAuth tokens or CPA API keys are recorded in this document.
