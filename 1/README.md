# Lesson 1


## WSL

```
wsl --install
```

## GITHUB


- зарегались на github.com
- создали репозиторий
- создали ключ ssh

```bash 
ssh-keygen -t ed25519 -C "mail" 
```

- сохранили приватный ключ
- закинули публичный на гитхаб (https://github.com/settings/keys)
- склонировали репу
  
```
git clone git@github.com:gigabotan/learn-code.git
```

## Python

# Mac
- Установить brew (https://brew.sh)

```
brew install python
```

# Linux/WSL

```
sudo apt update
sudo apt install python3 python3-pip
```

# Windows

```
winget install python
```