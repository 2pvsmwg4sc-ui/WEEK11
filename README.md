
# 성적 CSV 검증기

## ① 무엇을 하나요 (What · 현재 상태)

CSV 파일에서 이름과 점수를 읽어 유효한 데이터만 저장하고, 잘못된 데이터는 제외하는 프로그램입니다.

현재 pytest 테스트 12개를 통과했으며, 코드 커버리지는 80%입니다.

## ② 왜 만들었나요 (Why)

CSV 파일에 잘못된 점수나 빈칸이 있어도 정상적인 데이터만 사용할 수 있도록 만들었습니다.

또한 pytest를 활용하여 프로그램이 올바르게 작동하는지 확인하고, 오류를 발견하는 방법을 배우기 위해 작성했습니다.

## ③ 어떻게 쓰나요 (How)

### 실행 환경

- Python 3.13
- pytest 및 pytest-cov

### 설치

```powershell
python -m pip install pytest pytest-cov
```

### 프로그램 실행

```powershell
python load_scores.py scores.csv
```

실제 실행 결과:
- 읽은 줄: 5개
- 건너뛴 줄: 5개
- 유효한 데이터 5개가 정상적으로 출력됨
- 잘못된 데이터는 제외 사유와 함께 출력됨

### 테스트 실행

```powershell
python -m pytest test_load_scores.py -v
```

### 커버리지 측정

```powershell
python -m pytest test_load_scores.py --cov=load_scores --cov-report=term-missing
```

## ④ 어떻게 테스트하나요

### CSV 테스트

```powershell
python -m pytest test_load_scores.py -q
```

실제 결과: 12 passed

커버리지 측정 결과: 80% (미실행 줄 77~86)

### AI 테스트 실험

```powershell
python -m pytest test_bug_A.py -q
python -m pytest test_bug_B.py -q
```

- 실험 2-A (코드 제공): 3 passed, 1 failed
- 실험 2-B (명세 제공): 3 passed, 1 failed

두 실험 모두 마지막 원소가 최댓값인 경우의 버그를 발견했습니다.

`find_max([10, 20, 30])`의 기대값은 30이지만 실제 결과는 20입니다.

테스트 실패는 테스트 코드의 오류가 아니라 `find_max` 함수에 존재하는 버그를 발견한 결과입니다.

## ⑤ 파일 구성

| 파일 | 하는 일 |
| --- | --- |
| `load_scores.py` | CSV 파일을 읽고 유효한 데이터와 제외할 데이터를 구분하는 프로그램 |
| `scores.csv` | 프로그램 실행에 사용하는 예제 CSV 파일 |
| `empty.csv` | 빈 데이터 확인용 CSV 파일 |
| `weird.csv` | 잘못된 데이터가 포함된 CSV 파일 |
| `test_load_scores.py` | CSV 처리 기능을 검증하는 pytest 테스트 코드 |
| `bug3_logic.py` | 마지막 원소를 검사하지 않는 버그가 있는 함수 |
| `test_bug_A.py` | 코드를 제공하고 Copilot으로 생성한 테스트 |
| `test_bug_B.py` | 명세만 제공하고 Copilot으로 생성한 테스트 |
| `README.md` | 프로그램 설명, 실행 방법 및 테스트 결과를 정리한 문서 |

## ⑥ 만든 사람과 AI 사용

- 만든 사람: 강민수
- 사용한 AI 도구·모델: ChatGPT, GitHub Copilot Chat
- AI에게 도움받은 부분: ChatGPT를 활용해 실습 내용을 이해하고 테스트 방법을 학습했으며, Copilot으로 테스트 코드를 생성했습니다.
- 내가 직접 판단·확인한 부분: pytest를 직접 실행하여 테스트 결과를 확인하고, 마지막 원소를 검사하지 않는 버그를 발견했습니다.

## 라이선스

MIT License (`LICENSE` 파일 참고)
  
