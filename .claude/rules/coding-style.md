# Coding Style Rules

## Python
- PEP 8을 따른다.
- Type hint를 적극 활용한다.
- docstring은 Google 스타일을 사용한다.
- import 순서: 표준 라이브러리 → 서드파티 → 로컬 모듈 (각 그룹 사이 빈 줄)

## JavaScript / TypeScript
- ESLint + Prettier 설정을 따른다.
- `const` 우선, 필요할 때만 `let`. `var` 사용 금지.
- 비동기 처리는 async/await 패턴을 사용한다.
- TypeScript에서 `any` 타입 사용을 지양한다.

## 공통
- 함수는 한 가지 일만 한다 (Single Responsibility).
- 매직 넘버 대신 명명된 상수를 사용한다.
- 중복 코드가 3회 이상 반복되면 함수로 추출한다.
