
### [aws-s3 안내서]
> [참조 링크](https://docs.aws.amazon.com/ko_kr/AmazonS3/latest/dev/Welcome.html)

### \# Amazon S3이란 무엇?

+ Amazon S3(Simple Storage Service)는 인터넷용 스토리지 서비스.
+ Amazon S3에서 제공하는 단순한 웹 서비스 인터페이스를 사용하여 웹에서 언제 어디서나 원하는 양의 데이터를 저장하고 검색할 수 있음.

### \# Amazon S3 버킷을 사용한 작업

+ Amazon S3에 데이터(사진, 동영상, 문서 등)를 업로드하려면 우선 하나의 AWS 리전에 S3 버킷을 만들어야 함.
+ 그런 다음 이 버킷에 객체를 얼마든지 업로드할 수 있음. 
+ 구현 측면에서 버킷과 객체는 리소스.

### \# Amazon S3 객체로 작업

+ Amazon S3는 최대한 많은 객체를 저장할 수 있도록 설계된 단순한 키와 그 값의 스토어.
+ 객체의 구성 요소
	- Key : 객체에 지정한 이름입니다. 객체 키를 사용하여 객체를 검색.
	- Vesrsion ID : 버킷 내에서 키와 버전 ID를 사용하여 각 객체를 고유하게 식별할 수 있음.
	- Value(값) : 저장하는 콘텐츠.
	- Metadata : 객체 관련 정보를 저장하기 위한 이름-값 페어의 집합.
	- Subresources(하위리소스) : Amazon S3은 하위 리소스 메커니즘을 사용하여 객체 관련 추가 정보를 저장. 객체에 종속.
	- Access Control Information(액세스제어정보) : Amazon S3에 저장한 객체에 대한 액세스를 제어할 수 있음.

- - -

### [aws-s3 안내서 - 보안]
> [참조 링크](https://docs.aws.amazon.com/ko_kr/AmazonS3/latest/dev/access-control-overview.html)

### \# Amazon S3 리소스, 버킷 및 객체

+ AWS에서 리소스는 작업할 수 있는 객체.
+ Amazon S3에서 버킷 및 객체가 리소스이며 둘 다 연결된 하위 리소스가 있음.
+ 다음은 버킷 하위 리소스의 몇 가지 예..
	- lifecycle : 수명 주기 구성 정보를 저장.
	- website : 웹 사이트 호스팅용 버킷을 구성하려면 웹 사이트 구성 정보를 저장.
	- versioning : 버전 관리 구성을 저장.
	- policy and ACL : 버킷에 대한 액세스 권한 정보를 저장.
	- CORS(Cross-Origin Resource Sharing) : 교차 원본 요청을 허용하는 버킷 구성을 지원.
	- logging - Amazon S3에 요청해 버킷 액세스 로그를 저장.
	
### \# Amazon S3 버킷 및 객체 소유권

+ 기본적으로 리소스 소유자만 이러한 리소스에 액세스할 수 있음.
+ 리소스 소유자란 리소스를 생성한 AWS 계정을 말함.
+ 예.
	- 버킷 생성 및 객체 업로드에 사용하는 AWS 계정은 해당 리소스를 소유.
	- AWS IAM(Identity and Access Management) 사용자 또는 역할 자격 증명을 사용하여 객체를 업로드하는 경우 사용자 또는 역할이 속한 AWS 계정이 객체를 소유.
	- 버킷 소유자는 다른 AWS 계정(또는 다른 계정의 사용자)에 객체를 업로드할 수 있는 교차 계정 권한을 부여할 수 있음. 이 경우, 객체를 업로드하는 AWS 계정이 해당 객체의 소유자.

- - -

### \# Amazon S3 Block Public Access(퍼블릭액세스차단)의 사용

+ Amazon S3는 버킷 및 계정에 대한 퍼블릭 액세스 차단 설정을 제공하여 Amazon S3 리소스에 대한 퍼블릭 액세스를 관리하는 데 도움을 줌.
+ 기본적으로 새 버킷 및 객체는 퍼블릭 액세스를 허용하지 않지만 사용자는 퍼블릭 액세스를 허용하도록 버킷 정책 또는 객체 권한을 수정할 수 있음.
+ Amazon S3 퍼블릭 액세스 차단 설정은 이러한 정책 및 권한을 무시하므로 이러한 리소스에 대한 퍼블릭 액세스를 제한할 수 있음.
+ Amazon S3 퍼블릭 액세스 차단을 사용하면 계정 관리자 및 버킷 소유자가 리소스 생성 방식에 관계없이 적용되는 Amazon S3 리소스에 대한 퍼블릭 액세스를 제한하는 중앙 집중식 제어를 쉽게 설정할 수 있음.

#### \* 참고

+ 버킷 및 AWS 계정에 대해서만 퍼블릭 액세스 차단 설정을 활성화할 수 있음.
+ Amazon S3는 객체 단위로 퍼블릭 액세스 차단 설정을 지원하지 않음.
+ 계정에 퍼블릭 액세스 차단 설정을 적용하면 해당 설정은 전 세계 모든 AWS 리전에 적용.
+ 설정이 모든 리전에서 즉시 또는 동시에 적용되지는 않지만 결국 모든 리전으로 전파됨.

#### \* Block Public Access의 네 가지 설정
+ BlockPublicAcls
+ IgnorePublicAcls
+ BlockPublicPolicy
+ RestrictPublicBuckets

#### \* "퍼블릭"의 의미
> [참조 링크](https://docs.aws.amazon.com/ko_kr/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status)

+ ACL(액세스제어목록)
	- Amazon S3는 미리 정의된 AllUsers 또는 AuthenticatedUsers 그룹의 구성원에게 권한을 부여하는 경우 버킷 또는 객체 ACL을 퍼블릭으로 간주함.
+ Policies(정책)
	- 버킷 정책을 평가할 때 Amazon S3는 정책을 퍼블릭으로 가정하여 시작. 그런 다음 정책을 평가하여 비공개로 판단할 수 있는지 결정.

