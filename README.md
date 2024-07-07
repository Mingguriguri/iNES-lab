![header](https://capsule-render.vercel.app/api?type=waving&color=auto&height=200&section=header&text=INES_LAB&fontSize=50&animation=fadeIn&fontAlignY=35)
# iNES-LAB
This is our Lab web page (ver3)
> **바로가기: [https://ines-lab.com/](https://ines-lab.com/)**


### Main
 <img width="1822" alt="스크린샷 2024-07-07 오후 11 53 24" src="https://github.com/Mingguriguri/iNES-lab/assets/101111603/33b8511e-1c78-43a0-923c-e59e0d29dc08">
<img width="1822" alt="스크린샷 2024-07-07 오후 11 53 29" src="https://github.com/Mingguriguri/iNES-lab/assets/101111603/b533a87a-7c1f-4cd5-aec9-18541e98f29b">
<img width="1822" alt="스크린샷 2024-07-07 오후 11 53 33" src="https://github.com/Mingguriguri/iNES-lab/assets/101111603/e6184dc0-5408-4199-acf0-41bdbeef72d1">

- ver2와 바뀐 사항: 글씨체를 더 두껍게 수정하고, HW팀과 AI팀의 페이지를 구분하였다. (URL 패턴도 구분하고 버튼도 생성)

### Advisor
<img width="1822" alt="스크린샷 2024-07-07 오후 11 53 38" src="https://github.com/Mingguriguri/iNES-lab/assets/101111603/4fc1019e-5e4a-4406-8f3d-b19742748bee">

- 요구사항에 맞게 각 팀 페이지에 들어가면 첫 화면에는 교수님의 정보가 나오도록 설정하였다.

### Reseaarch
<img width="2032" alt="스크린샷 2024-07-01 오후 8 34 43" src="https://github.com/Mingguriguri/iNES-lab/assets/101111603/589f758f-39fd-4f7e-a460-789d986f12dc">

Project 내용 확인
<img width="2032" alt="스크린샷 2024-07-01 오후 8 34 57" src="https://github.com/Mingguriguri/iNES-lab/assets/101111603/3abc2529-c68c-470c-afe0-3927a621274f">

### Publication - Journal

### Publication - Conference

### Board - Notice

### Board - Awards

### Admin
> 관리자 페이지로, 연구실 멤버들이 각 페이지의 내용(데이터)을 추가,수정,삭제를 통해 웹페이지를 관리할 수 있는 영역이다.

<img width="1822" alt="스크린샷 2024-07-07 오후 11 54 50" src="https://github.com/Mingguriguri/iNES-lab/assets/101111603/a5dd6738-8476-4953-a0eb-ed73729e959e">


---

## 사전 준비
Python version: 3.12.3

## 프로젝트 설정

### 1단계: 저장소 클론

먼저, git을 사용하여 저장소를 로컬 컴퓨터에 클론합니다. 

```sh
git clone https://github.com/Mingguriguri/iNES-lab.git
cd iNES-lab
```
또는 저장소를 fork 한 후, 개인 저장소에서 클론합니다. 

### 2단계: 가상 환경 생성 (선택 사항)
종속성을 관리하고 다른 프로젝트와의 충돌을 피하기 위해 가상 환경을 생성하는 것을 권장합니다.
- Windows:
``` sh
python -m venv venv
venv\Scripts\activate
```

- macOS/Linux:
```sh
python -m venv venv
source venv/bin/activate
```

### 3단계: 종속성 설치
가상 환경을 활성화한 후, requirements.txt 파일에 나열된 종속성을 설치합니다.
```sh
pip install -r requirements.txt
```

### 4단계: 프로젝트 실행
프로젝트가 잘 실행되는지 확인해보세요!
```sh
python manage.py runserver
```

잘 실행된다면 프로젝트에 기여해주시면 됩니다 :D

### 가상환경 비활성화
```sh
deactivate
```

## 기여
1. 저장소를 포크하기
2. 새 브랜치를 생성하기 (git checkout -b feat/branch).
3. 변경사항을 적용하기
4. 변경사항을 커밋하기 (git commit -m 'feat: Add some feature'). 커밋할 때는 아래 커밋 컨벤션을 지켜주세요!
5. 브랜치에 푸시하기 (git push origin feature-branch).
6. 새 풀 리퀘스트를 생성하기

> **커밋 컨벤션, 브랜치, pull request 꼭 지키기 !**
> [[git][fork][bash] git bash로 협업하기 - Forking Workflow](https://co-deok.tistory.com/16)

### 사용
1. 이 레포를 fork해와서 개인 저장소로 가져옴
2. 각자 **본인 이름의 브랜치** 또는 **기능 이름의 브랜치**에서 작업한 내용을 본인 이름의 디렉토리에 올리고 `git push` (개인저장소), `git upstream`(팀 저장소) (자세한 건 위의 git bash 로 협업하기 블로그 내용 참조)
3. 최종적으로는 본인 이름의 리포지토리로 만들어서 합칠 예정 (git merge)


### 커밋 컨벤션
**1. 기능  : Feat, Fix, Design, !BREAKING CHANGE**  
- `Feat`: 새로운 기능을 추가할 경우  
- `Fix`: 버그를 고친 경우  
- `Design`: CSS 등 사용자 UI 디자인 변경  
- `!BREAKING CHANG`: 커다란 API 변경의 경우 (ex API의 arguments, return 값의 변경, DB 테이블 변경, 급하게 치명적인 버그를 고쳐야 하는 경우)  
- ex)"Feat(navigation): ~~~~  " "Fix(database): ~~~~"  

**2. 개선: Style, Refactor, Comment 태그**  
- `Style`: 코드 포맷 변경, 세미 콜론 누락, 코드 수정이 없는 경우 <오타 수정, 탭 사이즈 변경, 변수명 변경 등에 해당>   
- `Refactor`: 프로덕션 코드 리팩토링, 새로운 기능이나 버그 수정없이 현재 구현을 개선한 경우 <코드를 리팩토링 하는 경우>  
- `Comment`: 필요한 주석 추가 및 변경  
  
**3. 그 외: Docs, Test, Chore, Rename, Remove 태그**
- `Docs`: 문서를 수정한 경우  <README.md>  
- `Test`: 테스트 추가, 테스트 리팩토링 (프로덕션 코드 변경 없음)  <test 폴더 내부의 변경이 일어난 경우에만 해당>  
- `Chore`: 빌드 태스크 업데이트, 패키지 매니저 설정할 경우 (프로덕션 코드 변경 없음)  <package.json의 변경이나 dotenv의 요소 변경 등, 모듈의 변경에 해당>  
- `Rename`: 파일 혹은 폴더명을 수정하는 경우  
- `Remove`: 사용하지 않는 파일 혹은 폴더를 삭제하는 경우  
 
**4. 예시**  
- Feat: "추가 get data api 함수"  
-  "고침", "추가", "변경" 또는 "Fix", "Add", "Change" 사용  
