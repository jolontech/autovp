# Automation of generating and playing voice with voicepeak

## Requirement

- python >=3.10.9
- zsh 5.3 (x86_64-apple-darwin17.0)
- python modules in the ./requirements/requirements.txt
- voicepeak (`voicepeak.app/Contents/MacOS/voicepeak`)

```sh
% cd ./requirements/
% pip install -r requirements.txt
```


## How to use

```sh
% cd src
% python main.py [query] -o [out path] -v [vp path] -n [narrator] -e [emotion parameters]
```


## Example

```sh
% cd src
% python main.py 'テスト1。小春六花です' -o 'test1.wav'
% python main.py 'テスト2。宮舞モカです' -o 'test2.wav' -n 'Miyamai Moca'
% python main.py 'テスト3。おれはフリモメンだ！' -o 'test3.wav' -n 'Frimomen' -e 'happy=70,angry=10,sad=10,ochoushimono=100'
```

