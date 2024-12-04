# api_server_yj

# 프로젝트명: Kubernetes 기반 API 서버 배포

## 1. 환경 설정

### 1.1 Kubernetes 클러스터 구축
- **Minikube**를 사용하여 로컬 Kubernetes 클러스터를 구축

### 1.2 API 서버 설정
- **FastAPI**로 구현된 API 서버
- **MySQL DB**와 연동하여 CRUD 기능 제공

### 1.3 Helm을 이용한 배포
- MySQL은 **Bitnami Helm Chart**를 사용하여 배포
- API 서버는 `kubectl apply` 명령어로 배포

## 2. 인프라 구성도
(다이어그램 삽입)

## 3. 구축 완료 보고

### 3.1 배포 명령어
MySQL 설치:
```bash
helm install mysql bitnami/mysql --set auth.rootPassword=password --set primary.persistence.size=1Gi
