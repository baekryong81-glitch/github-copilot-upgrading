# upgraded 폴더 파일 구조 설명

`upgraded` 폴더는 레거시(`legacy`) 폴더의 전체 파일 및 디렉터리 구조를 복사하여 최신화 작업을 위한 공간입니다.

## 주요 구조

- `MANIFEST.in`, `README.rst`, `distribute_setup.py`, `setup.py`: 프로젝트 메타/설치 파일
- `guachi/`: 핵심 라이브러리 코드
  - `__init__.py`, `config.py`, `database.py`: 주요 모듈
  - `tests/`: 단위/통합 테스트 코드
    - `test_configurations.py`, `test_configmapper.py`, `test_database.py`, `test_integration.py`
- `guachi.egg-info/`: 패키징 정보 파일
  - `PKG-INFO`, `SOURCES.txt`, `dependency_links.txt`, `top_level.txt`
- `docs/`: Sphinx 기반 문서
  - `Makefile`: 문서 빌드용 Makefile
  - `source/`: 문서 원본(rst, conf.py, _static 등)
  - `build/`: 빌드된 문서(HTML, doctrees 등)

## 목적

- `upgraded` 폴더는 레거시 코드를 최신 Python 및 도구 체계로 이식/개선하는 실습 공간입니다.
- 원본과 동일한 구조를 유지하여 변경점 추적 및 테스트가 용이합니다.

---

> 이 구조를 바탕으로 각 파일/디렉터리의 역할과 위치를 쉽게 파악할 수 있습니다.
