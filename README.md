# 고급 Python 과정

중급에서 고급 Python 개발자를 위한 핵심 주제들을 다루는 프로그래밍 과정 자료입니다.

## GitHub Codespaces 환경 설정

이 저장소는 GitHub Codespaces에서 바로 실행할 수 있도록 구성되어 있습니다.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new)

환경 구성 내용:
- uv 패키지 매니저를 사용한 환경 설정
- Python 개발에 필요한 VS Code 확장
- Jupyter Lab 및 노트북 지원
- 생물정보학 라이브러리 포함

## 과정 구성

### Classes and Objects
**파일**: `Classes_and_Objects/21_classes_and_objects.md`

Python 객체지향 프로그래밍의 핵심 개념을 다룹니다:
- 클래스 정의와 객체 생성
- 속성과 메서드
- 상속, 캡슐화, 다형성
- 특수 메서드 (`__init__`, `__str__`, `__repr__`)
- 클래스 변수 vs 인스턴스 변수
- 정적 메서드와 클래스 메서드
- 프로퍼티와 게터/세터

### Decorators
**파일**: `Decorators/14_higher_order_functions.md`

함수형 프로그래밍 개념과 데코레이터 패턴을 학습합니다:
- 함수를 인자로 받는 고차함수
- 클로저의 개념과 활용
- 기본 데코레이터 작성법
- 매개변수를 받는 데코레이터
- 클래스 데코레이터
- functools.wraps 사용법
- 실제 사용 사례 (로깅, 타이밍, 캐싱)

### Exception Handling
**파일**: `Exception_Handling/15_python_type_errors.md`, `Exception_Handling/17_exception_handling.md`

Python에서 에러 처리와 예외 관리를 학습합니다:

**15_python_type_errors.md**:
- Python의 주요 에러 타입들
- TypeError, ValueError, KeyError 등
- 에러 메시지 해석 방법
- 스택 트레이스 읽기

**17_exception_handling.md**:
- try-except-finally 블록
- 여러 예외 처리
- 사용자 정의 예외 클래스
- 예외 체이닝
- 컨텍스트 매니저와 with 문

### API Development
**파일**: `API/API.md`

Python으로 API를 다루는 방법을 학습합니다:
- HTTP 요청의 기본 개념 (GET, POST, PUT, DELETE)
- requests 라이브러리 사용법
- JSON 데이터 처리
- 인증과 헤더 관리
- 에러 처리와 재시도 로직
- REST API 설계 원칙

### Pydantic 데이터 검증
**파일**: `Pydantic/1_pydantic_practice.ipynb`, `Pydantic/2_huggingface_practice.ipynb`

현대적인 데이터 검증과 파싱을 학습합니다:

**1_pydantic_practice.ipynb**:
- BaseModel을 사용한 데이터 모델 정의
- 타입 힌트와 자동 검증
- Field를 사용한 제약 조건 설정
- 중첩된 모델과 복잡한 데이터 구조
- 커스텀 검증기 작성
- JSON 직렬화/역직렬화
- 생물정보학 데이터 모델링 실습 (RNA-seq 데이터)

**2_huggingface_practice.ipynb**:
- HuggingFace API와 Pydantic 통합
- 머신러닝 모델 응답 데이터 검증
- API 응답 구조화

## 생물정보학 실습 노트북

### NCBI E-utilities 직접 활용
**파일**: `API/1_NCBI_Eutilities_HandsOn.ipynb`

HTTP 요청을 통한 NCBI 데이터베이스 직접 접근:
- E-utilities API 엔드포인트
- requests 라이브러리를 사용한 HTTP 요청
- XML 및 JSON 형태의 응답 처리
- 검색 쿼리 최적화

### Biopython과 NCBI 데이터베이스
**파일**: `API/2_Biopython_HandsOn.ipynb`

Biopython의 Entrez 모듈을 사용한 생물의학 데이터 수집:
- NCBI E-utilities API 개요
- Bio.Entrez 모듈 설정 (이메일, API 키)
- einfo: 데이터베이스 메타데이터 조회
- esearch: 검색어로 ID 목록 획득
- efetch: 상세 레코드 가져오기
- PubMed, PMC, ClinVar 데이터베이스 활용
- XML 응답 파싱과 데이터 구조화
- 대용량 데이터셋 생성 실습

## 개발 환경 설정

### GitHub Codespaces 사용
- 브라우저에서 바로 실행 가능
- 모든 의존성 자동 설치
- uv 패키지 매니저로 환경 구성

### 로컬 환경 설정
```bash
# uv 설치
curl -LsSf https://astral.sh/uv/install.sh | sh

# 가상환경 생성 및 의존성 설치
uv venv
source .venv/bin/activate  # Linux/Mac
# 또는 .venv\Scripts\activate  # Windows
uv pip install -r requirements.txt
```

## 포함된 패키지

**핵심 라이브러리**:
- huggingface: LLM 이용
- pydantic: 데이터 검증

**생물정보학**:
- biopython: 생물학적 데이터 처리

**웹/API**:
- requests: HTTP 요청
- httpx: 비동기 HTTP 클라이언트
- python-dotenv: 환경변수 관리

**개발 도구**:
- jupyter: 노트북 환경

## 사전 요구사항

- Python 기초 지식 (변수, 데이터 타입, 제어문)
- Python 3.12 이상
- 명령줄 기본 사용법

## 생물정보학 API 설정

NCBI E-utilities 사용을 위한 환경변수 설정:

```bash
# .env 파일 생성
EUTILS_EMAIL=your.email@example.com
EUTILS_API_KEY=your_ncbi_api_key_here  # 선택사항
EUTILS_TOOL=python-bioinformatics-course
```

## 추가 학습 자료

- [Pydantic 공식 문서](https://docs.pydantic.dev/)
- [Biopython 튜토리얼](http://biopython.org/DIST/docs/tutorial/Tutorial.html)
- [NCBI E-utilities 가이드](https://www.ncbi.nlm.nih.gov/books/NBK25497/)