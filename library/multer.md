인코딩 타입: multipart/form-data인 경우 데이터 처리용 모듈

변수에 multer() 를 할당해 미들웨어를 생성하는 개체로 만듬
storage 속성: 파일 저장 방식과 경로, 파일명 등 설정
    diskStorage 속성: 이미지 서버 디스크에 저장, 저장 경로 설정
    filename: 파일 이름 설정

multer의 미들웨어
    single:
        이미지 하나는 req.file로
        나머지 정보는 req.body로
    
    array(어레이는 하나의 속성에 여러 개 업로드),
    fields(필즈는 여러 개의 속성에 이미지를 하나씩 업로드):
        이미지들은 req.files로
        나머지 정보는 req.body로
        
    none:
        모든 정보를 req.body로
    