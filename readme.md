[CampuspeLogo](https://campuspe.com/logo1.svg)

# Campuspe Generative AI Class


## Virtual Environment

1. What is Virtual Environment?
A isolated Python Enviromen that lets you:
- Install Project spefic packages without affecting other projects
- Use different packages for different projects
- Avoid dependency conflicts between projects
- Project coordination easy 

```
Project A -> venv_a -> TensorFlow 2.10
Project B -> venv_b -> TensorFlow 2.12

```

2. Commands to Run Venv
- Windows
```
cd project-name
python -m venv <venv-name(replace with actual env name)>
<venv-name\Scripts\activate>
deactivate

```
- Mac and Linux and unix os
```
cd project-name
python -m venv <venv-name(replace with actual env name)>
source <venv-name>/Scripts/activate
deactivate

```