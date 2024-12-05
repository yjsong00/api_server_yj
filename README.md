# api_server_yj

# 프로젝트명: Kubernetes 기반 API 서버 배포

## 1. 환경 설정

### 1.1 Kubernetes 클러스터 구축
- **Minikube**를 사용하여 로컬 Kubernetes 클러스터를 구축

### 1.2 MYSQL DB 설정
- MySQL은 **Bitnami Helm Chart**를 사용하여 배포
- 수동으로 db create, item 테이블 속 name, description 칼럼 추가

### 1.3 API 서버 설정
- **FastAPI**로 구현된 API 서버
- **MySQL DB**와 연동하여 CRUD 기능 제공
- DB 연결을 위해 `mysql-connector-python` 라이브러리를 사용
- **dockerhub**에 이미지 푸쉬

### 배포 명령어
MySQL 설치:
```bash
helm install mysql bitnami/mysql --set auth.rootPassword=password --set primary.persistence.size=1Gi
mysql -h mysql -u root -p
docker build -t <도커허브주소>/api-server:<태그>
