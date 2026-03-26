# 🏷️ Deal Tracker (Python)
> **Universal Price Monitor for Digital Contents** > **디지털 콘텐츠를 위한 범용 가격 모니터링 시스템**

This project is a TDD-based automated tool designed to monitor price fluctuations across various digital storefronts (Games, Movies, Apps) through an abstracted architecture.
본 프로젝트는 추상화된 아키텍처를 통해 다양한 디지털 스토어(게임, 영화, 앱 등)의 가격 변동을 감시하고 알림을 보내는 TDD 기반의 자동화 도구입니다.

---

## 🚀 Project Goals / 프로젝트 목표
- **Abstraction (추상화):** Minimize code changes when adding new stores or notification methods. (새로운 스토어나 알림 수단 추가 시 기존 코드 수정을 최소화합니다.)
- **Data Efficiency (데이터 효율성):** Save history only when prices change and prevent redundant checks. (가격 변동이 있을 때만 이력을 저장하고, 중복 체크를 방지합니다.)
- **TDD (테스트 주도 개발):** Verify all core logic through test codes during development. (모든 핵심 로직은 테스트 코드를 통해 검증하며 개발합니다.)
- **Scalability (확장성):** Maintain a design that considers future Telegram interactive bots and porting to Rust. (향후 Telegram 대화형 봇 도입 및 Rust 언어로의 포팅을 고려한 설계를 유지합니다.)

## 🛠️ Tech Stack / 기술 스택
- **Language:** Python 3.10+
- **Database:** SQLite (via SQLAlchemy ORM)
- **Test:** pytest, pytest-mock
- **Library:** requests, python-dotenv

---

## 📅 TODO List / 구현 로직

### Phase 1: Foundation & Abstraction / 기초 및 추상화
- [ ] **Setup Project & Environment** / 프로젝트 구조 및 가상환경 설정
- [ ] **Define Store Base Class** / `Store` 추상 베이스 클래스 정의 (`base.py`)
- [ ] **Implement StoreFactory** / URL 패턴 분석 및 스토어 판별을 위한 팩토리 구현
- [ ] **Design DB Models** / SQLAlchemy 기반 DB 모델 설계 (`Product`, `PriceHistory`)

### Phase 2: Store Implementation / 스토어 구현
- [ ] **Implement Nintendo Store** / 닌텐도 스토어 연동 (NSUID 추출 및 API 호출)
- [ ] **Implement Apple Store (App/Movie)** / 애플 스토어 연동 (앱 및 영화 가격 로직)
- [ ] **Expand to Generic Stores** / 향후 구글 플레이 등 타 스토어 확장 기반 마련

### Phase 3: Monitoring Logic / 모니터링 고도화
- [ ] **Price Change Detection** / 가격 변동 여부 판단 로직 (변동 시에만 저장)
- [ ] **Duplicate Check Prevention** / 중복 체크 방지 (12시간 내 체크 기록 있을 경우 Skip)
- [ ] **Data Cleanup** / 데이터 클리닝 (3~5년 이상 된 오래된 이력 자동 삭제)

### Phase 4: Notification System / 알림 시스템
- [ ] **Define Notifier Base Class** / `Notifier` 추상 베이스 클래스 정의
- [ ] **Telegram Notifier:** Implement one-way discount alerts / 단방향 할인 알림 발송 기능
- [ ] **Optimize Message Template** / 메시지 템플릿 최적화 (콘텐츠 타입별 구분)

### Phase 5: Interactive Interface / 대화형 인터페이스
- [ ] **Telegram Bot Interaction** / 텔레그램 봇 기반 상호작용 (URL 전송 시 자동 등록)
- [ ] **List Tracking Items** / 현재 추적 중인 리스트 조회 명령 구현

---

## 🚦 Getting Started (TDD) / 시작하기
To run tests, use the following command:
테스트를 실행하려면 다음 명령어를 입력하세요:
```bash
pytest
