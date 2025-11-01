# Week 3 Assignment — Unity Scene with Imported Maze (15 pts)

## Overview
Create a Unity 3D scene that imports your Blender maze (from Week 1/2) via FBX, assigns materials, and configures basic physics so a sphere rests on the maze floor. Organize assets into Scenes, Models, Materials, Prefabs.

## Requirements
- Project & Scene Setup (3 pts)
  - Unity 2022 LTS 3D project
  - Folders: Assets/Scenes, Assets/Models, Assets/Materials, Assets/Prefabs
  - Save scene: Assets/Scenes/Week03_Maze.unity
- FBX Import (4 pts)
  - Export FBX from Blender (Apply Modifiers ON)
  - Import to Assets/Models, Scale Factor 1.0
  - Extract materials to Assets/Materials
- Materials & Appearance (3 pts)
  - Assign appropriate materials to maze elements
  - Shader: Standard or URP/Lit
- Physics (3 pts)
  - Colliders on environment (Box/Mesh)
  - Sphere with Rigidbody + SphereCollider rests on floor

## Submission
- Commit and push your Unity project folder to GitHub under `week-03/`
- Include FBX and scene file

## Tips
- If materials appear pink, extract materials and reassign textures
- Apply scale/rotation in Blender (Ctrl+A) before exporting FBX
- Keep Console clean; fix import warnings where possible

