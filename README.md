<h4 align='center'> 농림축산식품부ㅣ농림수산식품교육문화정보원 </h4>

<h1 align='center'> 2023 스마트농업AI 경진대회 </h1>

<p align='center'> 머신러닝 학습을 통한 최적의 토마토 재배 모델(복합제어환경) 개발 </p>

<h3 align='center'> 🍅  </h3>

<div align='center'>

<table>
    <thead>
        <tr>
            <th colspan="5"> 팜하니 </th>
        </tr>
    </thead>
    <tbody>
        <tr>
          <tr>
            <td align='center'><a href="https://github.com/noooey"><img src="https://avatars.githubusercontent.com/u/66217855?v=4" width="100" height="100"></td>
            <td align='center'><a href="https://github.com/YunHaaaa"><img src="https://avatars.githubusercontent.com/u/63325450?v=4" width="100" height="100"></td>
            <td align='center'><a href="https://github.com/Jaejuna"><img src="https://avatars.githubusercontent.com/u/37354854?v=4" width="100" height="100"></td>
          </tr>
          <tr>
            <td align='center'>박규연</td>
            <td align='center'>윤하은</td>
            <td align='center'>정재준</td>
          </tr>
        </tr>
    </tbody>
</table>

</div>

&nbsp; 

## 성능
|        |RMSE|R2 Score |비고|
|--------|--------|-----|----|
|01_autogluon|3615.5786537397207|0.9999623472368988|사용X|
|02_LR|239118.89780125386|0.5190696540948687|
|03_RF|59106.108669295354|0.9551833567393095||
|04_autogluon|7039.3037549989185|0.9998572748078142|사용X|
|05_RF|32681.894056635512|0.9940656660989127|반영X|
|11_TE_St_X|26353.363510935025|0.9976384597238256|반영X|
|13_TE_St_Lg|22511.365733378607|0.9983668580788365||

## File Directory
```bash
├── data
│   ├── train
│   ├── test
│   └── validation
├── EDA
│   └── eda
├── 1st
│   ├── model_1.ipynb
│   └── README.md
├── 2nd
│   ├── model_2.ipynb
│   └── README.md
├── 3rd
│   ├── model_3.ipynb
│   └── README.md
├── 4th
│   ├── model_4.ipynb
│   └── README.md
└── README.md
```

---

## dependency install manual
**conda env create 예시**
```python
# conda create -n {env_name} pyhton=3.9 
# conda activate {env_name}
```
**autogluon install 예시**
```python
# pip install -U pip
# pip install -U setuptools wheel
### default: autogluon==0.8.2
# pip install autogluon  
# pip install sklearn
```

**how to train**
```python
# python autogluon.py

```

**how to evaluate**
```python
# TBD
```

### autogluon trouble shooting
- 다른 프레임워크나 라이브러리 사용할 경우 version confilct 발생할 가능성 있음
- (맥의 경우) autogluon 설치 시 해당 오류 발견 시: 'ERROR: Could not build wheels for lightgbm, which is required to install pyproject.toml-based projects' 터미널에서 다음을 설치:
```python
# brew install cmake
``` 
- - 이 외의 의존성 문제는… 화이팅…!
- 원하는 만큼의 성능이 안 나올 시, autogluon 결과를 토대로 다른 모델을 강구해야 할 수 있음

### train log 
**autoGluon result**
In order of (hyperparam, stack and bag num, train hour, evaluation metric for train, etc)
1. RMSE: 3615.5786537397207, R2_score: 0.9999623472368988 (default, default, 1hr, RMSE, suspecting bug in the code: nope)
2. RMSE: 7039.3037549989185, R2_score: 0.9998572748078142 (GBM(lightGBM), 2, 1hr, RMSE)
## Citation:
#### Erickson, Nick, et al. "AutoGluon-Tabular: Robust and Accurate AutoML for Structured Data." 
#### arXiv preprint arXiv:2003.06505 (2020).
