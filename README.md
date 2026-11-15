# create.thumbnail

Create and revise Roblox promotional artwork with ChatGPT image generation. Describe a scene or attach reference art, and ask for a thumbnail or game icon.

| Output | Size | Downloads |
| --- | --- | --- |
| Roblox thumbnail | 1920 × 1080 | PNG and JPEG |
| Roblox game icon | 512 × 512 | PNG and JPEG |

## Install in ChatGPT desktop

1. Install the [ChatGPT desktop app](https://chatgpt.com/download/) and the [Codex CLI](https://developers.openai.com/codex/cli/).
2. In a terminal, run:

   ```sh
   codex plugin marketplace add LobbyCraft/create.thumbnail
   ```

3. Restart ChatGPT desktop. In Work mode or Codex, open **Plugins**, select the **LobbyCraft** marketplace, and install **create.thumbnail**.
4. Start a new chat in a mode with image generation and file processing, select **create.thumbnail**, and describe what you want to make.

See [OpenAI's marketplace setup guide](https://developers.openai.com/plugins/build/plugins#add-a-marketplace-from-the-cli). Availability of image generation and file exports depends on the ChatGPT mode and account. This GitHub distribution targets the desktop marketplace. Render generation uses ChatGPT's image tools.

## Update create.thumbnail

Close ChatGPT desktop, then refresh the LobbyCraft marketplace from GitHub and install the current plugin files:

```sh
codex plugin marketplace upgrade lobbycraft
codex plugin add create-thumbnail@lobbycraft
```

Reopen ChatGPT desktop and start a new chat. If it still loads an older copy, run the uninstall command below, then run the install command again.

## Codex CLI command reference

| Action | Command |
| --- | --- |
| Add the marketplace | `codex plugin marketplace add LobbyCraft/create.thumbnail` |
| List configured marketplaces | `codex plugin marketplace list` |
| List LobbyCraft plugins | `codex plugin list --marketplace lobbycraft --available` |
| Install create.thumbnail | `codex plugin add create-thumbnail@lobbycraft` |
| Refresh the marketplace from GitHub | `codex plugin marketplace upgrade lobbycraft` |
| Uninstall create.thumbnail | `codex plugin remove create-thumbnail@lobbycraft` |
| Remove the marketplace | `codex plugin marketplace remove lobbycraft` |

## In-chat plugin commands

In ChatGPT Work, type `@` and select **create.thumbnail** from the picker, then describe what you want to make or change.

```text
@create.thumbnail Make a Roblox thumbnail of two avatars jumping across lava.
@create.thumbnail Analyse these attached images and give me a reusable thumbnail style brief.
```

In Codex, use the `$` picker to select either skill directly. The picker may show the plugin name alongside the skill name.

| Skill | What it does | Example in Codex |
| --- | --- | --- |
| `create-thumbnail` | Generates thumbnails and game icons, edits artwork, and exports PNG or JPEG files. | `$create-thumbnail Make a 512 × 512 game icon of a Roblox avatar hanging from a ceiling.` |
| `thumbnail-reference-intake` | Analyses reference images and turns them into a reusable style brief. | `$thumbnail-reference-intake Analyse these three screenshots and list the style choices I should reuse.` |

Thumbnail, icon, edit, and export requests all use the creation skill. Describe the specific action in your prompt.

## Prompts to use in ChatGPT

- Create a Roblox thumbnail of two blocky avatars jumping between lava platforms. Put the checkpoint in the distance and leave text off.
- Create a game icon of a Roblox avatar in sticky boots clinging to a ceiling. Export PNG and JPEG.
- Analyse these reference images and give me a reusable style brief for future thumbnails.
- Export my latest thumbnail as JPEG only.
- Move only the flashlight into the character's hand in my last thumbnail. Match the grip to the handle.

Attach your artwork or face decal when an exact visual match matters. The public package includes source links and design notes for Roblox market examples and official classic faces. Reference images can be supplied in chat.

Version 0.4.4 adds the [November 2026 market benchmark](plugins/create-thumbnail/skills/create-thumbnail/references/market/README.md), with 4,466 reference links and 63 individually annotated examples. The skill uses these to compare marketplace artwork against the requested scene at full size and mobile preview size.

For install or export problems, open an issue in [GitHub Issues](https://github.com/LobbyCraft/create.thumbnail/issues).
