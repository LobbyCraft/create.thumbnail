---
name: create-thumbnail
description: Create or revise Roblox promotional thumbnails (1920 x 1080) and game icons (512 x 512) from scene prompts or visual references. Use for create.thumbnail requests, Roblox thumbnail artwork, and Roblox game icon generation.
---

# create.thumbnail

Create the actual image using the host image-generation tool, not merely a prompt. This is a skills-only plugin using host capabilities; it does not include an image model, analytics connection, Roblox upload tool, or standalone editor. If image generation is unavailable, explain the limitation and provide a ready-to-run art brief without pretending an image was generated.

## Resolve the request

- Support two formats, defined in [formats.json](references/formats.json): thumbnail = 1920 × 1080, 16:9; game icon = 512 × 512, 1:1. Keep these separate and make adding future formats straightforward.
- Respect an explicit format. A scene-only request defaults to the landscape thumbnail. Ask which format only when both are equally plausible; request both only when the user wants both.
- Extract the subject, number of characters, action, setting, emotional hook, must-have objects, text, and supplied references. Preserve unusual scene details rather than replacing the idea with generic promotional art.
- Use sensible defaults when the scene is sufficient. Ask one concise bundled question only if missing information materially changes the result. Do not require a long questionnaire or approval round before generation.
- Default to a polished, colourful Roblox 3D game render with no text when the brief gives no style direction. Select a relevant visual family from the supplemental playbook and inspect any supplied reference images. Current instructions and task-specific references override the baseline; do not force bright daylight, expressive faces or studs when the chosen family calls for a different treatment.

## Match professional Roblox references

Read the [market benchmark](references/market/README.md). Start with its annotated examples and choose one close reference for the gameplay hook and another for the visual finish. Open the actual images where accessible. Compare framing, perspective, pose clarity, silhouette, lighting and materials, and carry those craft choices into an original arrangement for the requested game. Use the user's scene and supplied images as the primary direction. Leave source branding, watermarks and unrelated claims out of the output.

Compare the draft with the references at full size and at roughly 320 × 180 for landscape thumbnails. Check the focal action, clean edges, readable silhouettes, plausible contact and consistent light. Make targeted corrections when available. When the source cannot be viewed, use another source or the supplied artwork.

## Approved characters for thumbnails — STRICT CHARACTER LOCK

**Authoritative user direction (2026-11-18): ONLY use the five characters in the bundled turnaround sheets for every thumbnail that contains any characters.** Do not create generic Roblox avatars, background extras, reskinned variants, or figures from market references. Use the actual reference image for each chosen character, never just a verbal likeness description. Treat the character's body silhouette, hair, hands, clothing, shoes, skin and accessories as fixed identity traits, changing only pose, expression (within the existing face rules), orientation, and camera framing. Character-free thumbnails are unaffected; square game icons retain their separate identity workflow unless the user later changes it. If a requested design is outside the roster, ask to change the roster first.

For any thumbnail containing characters, use only the five characters in the [approved roster](references/characters/README.md). Apply this to every visible figure, including background characters and thumbnail revisions. Open and attach the actual sheet for each selected identity. For a thumbnail, these sheets govern identity and body shape over older character baselines, market examples and generic rig defaults. Scene references can guide layout, lighting and poses. Character-free thumbnails skip these steps. The existing character workflow for square game icons continues below.

## Character and face references

For game icons, read [character-baselines.md](references/character-baselines.md) when a Bacon Boy or Bacon Girl appears. The attached Bacon Girl reference is authoritative: red/orange bun hair with swept fringe and side locks, white/light-grey head and C hands, teal denim jacket, grey/white striped shirt, burgundy trousers and black shoes. Preserve her supplied Roblox proportions.

For thumbnails, preserve the approved character identity and consult the roster’s face guidance. For game icons, use a supplied reference when the user requests a specific face. For official Roblox classic faces, see [face selection](references/face-selection.md) and [the catalogue](references/official-faces.tsv). Match the expression to the scene, keep its scale proportionate to the head, and use the full face design. If a face is essential and its texture is unavailable, ask the user to attach it. The image generator may approximate decals, so verify fidelity before describing a match as exact.

## Build the image

Read [art-direction.md](references/art-direction.md) and the [supplemental thumbnail playbook](references/thumbnail-playbook.md). Turn the scene into a concise art brief and send it to image generation. Include the selected output dimensions, aspect ratio, character anatomy, action and spatial relationships, camera, lighting, focal hierarchy, colours, background, and exclusions.

Characters must read immediately as Roblox humanoids: blocky heads and torso, squared limbs, toy-like hands and feet, simplified faces, recognisable Roblox avatar proportions. Match the selected roster sheet’s proportions in thumbnails. In game icons, prefer classic blocky R6-like proportions unless a supplied avatar reference calls for a different Roblox rig. Avoid realistic human anatomy, realistic skin detail, five-finger human hands, or generic smooth cartoon humans. Gender presentation follows the request through hair, outfit, face and accessories without sexualisation or degrading stereotypes. Characters should have distinct silhouettes and clearly readable emotions.

Generate one polished image by default. If variants are requested, vary a meaningful composition or emotional hook and preserve the actual game premise. Follow the current image tool's reference, transparency, and output-display rules. Inspect local reference files before editing and pass the actual references through supported tool inputs. Default to an opaque full-bleed scene, not a transparent cutout.

For revisions, use the selected previous output as the edit canvas. Use the smallest targeted change that satisfies the request and compare the result with the previous output. See the supplemental playbook for how to distinguish the edit target from style references.

## Quality and delivery

- Check scene fidelity, Roblox anatomy, character count, object placement, coherent contact/poses, facial readability, edge cropping and mobile-size readability. Correct a material mismatch using image editing when available.
- Request the exact target resolution. Inspect available output dimensions, rather than assuming that specifying a size in the prompt guarantees it. If the host produces a different size, use a supported export/resampling workflow to provide final PNG and JPEG exports at the exact dimensions. Preserve aspect ratio; never stretch anatomy. Prefer an image edit/outpaint to repair framing before cropping. Technical export size normalisation must not redraw the artwork.
- For game icons, a larger square generation may be used as the working master. Export the final PNG and JPEG at exactly 512 × 512 using high-quality downsampling (such as Lanczos), without stretching or repeated resizing. Check readability at 150 × 150 as well as at full export size. Avoid fine details that disappear at preview size.
- Verify the exported file's pixel dimensions before labelling it 1920 × 1080 or 512 × 512. If exact-size export is unavailable, state the actual dimensions and the limitation plainly; do not claim the requested resolution was delivered.
- Display generated images using the host's required image output mechanism. Save separately created export files through the host's persistent-file workflow when available. Do not download or re-upload an automatically saved generated image merely to display or save it.
- Keep the response short. After a delivered image, an optional next-step question can ask which specific change the user wants; omit extra prose where the image tool requires image-only output.
- Say 'designed for click appeal' or 'CTR-focused', never promise high CTR, invent performance metrics, or treat taste as measured conversion. Actual CTR must come from real testing. Do not browse unless the request needs research or current platform requirements.

## Download formats

- Offer downloadable **PNG and .jpeg versions** of each final image by default, unless the user requests only one. Both files must depict the same approved artwork and have the selected target dimensions; do not generate separate pictures for different encodings.
- JPEG is an additional option; retain PNG support. Use the actual .jpeg extension and image/jpeg encoding, not a renamed PNG. Accept requests for JPG as the same encoding but use .jpeg for default downloads.
- Use [export_image.py](scripts/export_image.py) for technical resizing and encoding when a local approved master is available: `python scripts/export_image.py INPUT --kind game-icon --output-dir OUTPUT`. For thumbnails use `--kind thumbnail`; `--format jpeg` or `--format png` exports only the requested format. The default exports both. Pillow is required; do not silently switch image-generation providers if unavailable.
- The exporter uses Lanczos downsampling, an RGB JPEG at quality 95 with no chroma subsampling, and no repeated lossy saves. Preserve a lossless master. JPEG cannot retain alpha; composite transparent input on the user-selected background (white by default) and disclose that when relevant. Use `--background '#RRGGBB'` to choose it.
- Never stretch or silently crop a mismatched aspect ratio. The exporter rejects it; reframe through the image tool first. A larger correctly proportioned master is preferred, and do not upscale a small master without explaining its quality limits.
- Verify each output's actual encoding and pixel size. Save separately created downloads using the host's persistent-file workflow and supply distinct labelled PNG and JPEG download links. If local bytes or file export are unavailable, explain that JPEG download is unavailable in that session instead of inventing a file or link. Do not retrieve an automatically saved generated image solely to redisplay it; creating a specifically requested alternate encoding is an export operation.

## Visual references

Use the user's supplied images as the primary scene direction. For thumbnails, use the approved roster for every character identity. The [November 2026 market benchmark](references/market/README.md) and [earlier market examples](references/market-examples.json) provide provenance links and visual notes for selected Roblox titles. Open the source if available and relevant. If a source is unavailable, continue with the user's references and the playbook. Chart placement and player counts do not establish image-level CTR.

Use the sibling thumbnail-reference-intake skill to analyse new references for a brief.
