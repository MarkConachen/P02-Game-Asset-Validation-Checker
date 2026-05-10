# Game Asset Validation Checker

**GitHub Repository URL:**  
https://github.com/MarkConachen/P02-Game-Asset-Validation-Checker

## Description

Game Asset Validation Checker is a Maya Python tool made to help game/digital artists and students prepare selected assets before exporting them. The tool checks for common game asset problems such as default Maya names, invalid naming characters, unfrozen rotation or scale, objects not being at the world origin, construction history, missing material assignments, and geometry issues. It gives the user a clear validation report so they can see what passed and what needs attention.

This tool is meant for digital artists, game art students, and anyone preparing models for a game pipeline. Users can run validation, fix safe issues, rename selected objects with a prefix, prepare and validate assets in one workflow, select failed objects, and export selected assets as an FBX once validation passes. The goal of the tool is to make the asset production workflow faster, more organized, and easier to understand before sending models to a game engine.

## Main Features

- PySide2 interface built for Maya
- Checks selected objects for common game export problems
- Detects default Maya names and invalid name characters
- Checks if rotation and scale are frozen
- Checks if objects are at the world origin
- Checks for construction history
- Checks for material assignment
- Checks for geometry issues
- Gives a clear validation report
- Fixes safe issues automatically
- Renames selected assets with a custom prefix
- Selects failed objects after validation
- Enables FBX export only when validation passes

## Challenge Features

- Validation report that shows pass and warning messages for each selected object
- Safe fix system that freezes rotation and scale, deletes construction history, and centers pivots
- Prefix-based batch renaming system
- Select Failed Objects button for quickly finding problem assets
- FBX export button that only unlocks after the selected assets pass validation
- Polished PySide2 layout with organized sections for naming, checks, actions, and report output

## How to Use

1. Open Maya.
2. Run the Python script in Maya's Script Editor.
3. Select one or more objects in the scene.
4. Click **Run Validation** to check the selected assets.
5. Use **Fix Safe Issues** to clean safe problems.
6. Enter a prefix and click **Rename Selected** if needed.
7. Click **Prepare + Validate** to run the main workflow.
8. If objects fail, click **Select Failed Objects** to find them.
9. Once validation passes, click **Export Selected FBX**.

## Notes

This tool does not automatically fix every possible issue because some changes could damage an artist's model. Riskier problems, such as geometry issues or object placement, are reported so the artist can review and fix them manually. Material assignment also fit into this category. 