# Xiao Mo Look Mechanics

## Natural motion

Xiao Mo is a compact humanoid with a separate head and body. His boots, lower legs, and pelvis stay registered and grounded. The eyes lead each gaze; eyelids and brows reshape with the target, then the head and neck turn or pitch subtly, with restrained upper-torso follow-through. The skull, facial proportions, tattoos, clothing, and hands must not warp. His hair follows the head as one coherent mass with only slight tip lag.

The belt chain, amber waist beads, and left-side handkerchief remain attached to their exact anchor points. They follow the torso with very small continuous lag and must never flip sides, detach, or teleport. Earrings rotate with the head and may become partly occluded on the far side. No whole-sprite rotation, affine tilt, broad raster warp, or pupil-only shortcut.

## Stable identity and motion budget

- Keep boots, lower-body center, scale, and baseline stable in all directions.
- Preserve the warm mischievous expression, tousled black mullet, warm tan skin, dark-brown eyes, silver ear hoops, tattoos, houndstooth vest, wide trousers, chain, beads, and handkerchief.
- Every 22.5-degree step changes eye aim, eyelids, head yaw or pitch, and upper-body follow-through by a similar visual amount.
- Keep both eyes anatomically inside the face; rotate/redraw the complete visible eye surfaces with compatible eyelid and brow changes.
- Intermediate poses form one continuous clockwise family. No adjacent snap, side flip, scale pop, registration jump, or prop detachment.

## Cardinal pose families

- `000 up`: eyes and pupils clearly above neutral, upper eyelids open toward the top; chin lifts slightly and the face pitches upward. Both body sides remain balanced, with a subtle upward chest follow-through. Hairline and brows stay stable; no whole-body lean.
- `090 screen-right`: pupils, nose tip, face plane, chin, and head turn unmistakably toward the image's right edge. More of Xiao Mo's screen-left cheek and screen-left body side is visible; the screen-right side recedes and is partly occluded. Earrings on the far side reduce in visibility. Chain and handkerchief stay attached and lag only slightly.
- `180 down`: eyes and pupils clearly below neutral, upper eyelids lower and brows soften; chin tucks and the face pitches downward. Hair may overlap the forehead slightly more, while the torso remains centered and feet stay fixed.
- `270 screen-left`: pupils, nose tip, face plane, chin, and head turn unmistakably toward the image's left edge. More of Xiao Mo's screen-right cheek and screen-right body side is visible; the screen-left side recedes and is partly occluded. Earrings on the far side reduce in visibility. Chain and handkerchief stay attached and lag only slightly.

## Interpolation and boundaries

Row 9 runs `000 -> 022.5 -> 045 -> 067.5 -> 090 -> 112.5 -> 135 -> 157.5`, evenly blending up through screen-right toward down. Row 10 runs `180 -> 202.5 -> 225 -> 247.5 -> 270 -> 292.5 -> 315 -> 337.5`, evenly blending down through screen-left toward up. The `157.5 -> 180` and `337.5 -> 000` boundaries must each move exactly one visual step with no pose reset.
