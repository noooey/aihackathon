# aihackathon
**팀명: 팜하니** 
팀원: 박규연 (팀장), 윤하은, 정재준

## autogluon manual
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
```

**how to use**
```python
# python autogluon.py

```

### autogluon trouble shooting
- 다른 프레임워크나 라이브러리 사용할 경우 version confilct 발생할 가능성 있음
- (맥의 경우) autogluon 설치 시 해당 오류 발견 시: 'ERROR: Could not build wheels for lightgbm, which is required to install pyproject.toml-based projects' 터미널에서 다음을 설치:
```python
# brew install cmake
``` 
   - 이 외의 의존성 문제는… 화이팅…!
- 원하는 만큼의 성능이 안 나올 시, autogluon 결과를 토대로 다른 모델을 강구해야 할 수 있음

## Citation:
#### Erickson, Nick, et al. "AutoGluon-Tabular: Robust and Accurate AutoML for Structured Data." 
#### arXiv preprint arXiv:2003.06505 (2020).
