<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>

<!DOCTYPE html>
<html>

<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
<meta name="description" content="" />
<meta name="author" content="" />
<title>분석결과</title>

<!-- Favicon-->
<link rel="icon" type="image/x-icon" href="assets/img/instagram.ico" />

<!-- Font Awesome icons (free version)-->
<script src="https://use.fontawesome.com/releases/v5.15.3/js/all.js"
	crossorigin="anonymous"></script>
	
<!-- Google fonts-->
<link href="https://fonts.googleapis.com/css?family=Montserrat:400,700"
	rel="stylesheet" type="text/css" />
<link
	href="https://fonts.googleapis.com/css?family=Lato:400,700,400italic,700italic"
	rel="stylesheet" type="text/css" />
	
<!-- Core theme CSS (includes Bootstrap)-->
<link href="css/styles.css" rel="stylesheet" />
</head>


<body id="page-top">
	<!-- Navigation-->
	<nav class="navbar navbar-expand-lg bg-secondary text-uppercase fixed-top" id="mainNav">
		<div class="container">
			<a class="navbar-brand js-scroll-trigger" href="/TAG_ME/TAG-ME/HOME.jsp">TAG ME</a>
			<button
				class="navbar-toggler navbar-toggler-right text-uppercase font-weight-bold bg-primary text-white rounded"
				type="button" data-toggle="collapse" data-target="#navbarResponsive"
				aria-controls="navbarResponsive" aria-expanded="false"
				aria-label="Toggle navigation">
				Menu <i class="fas fa-bars"></i>
			</button>
			
			<div class="collapse navbar-collapse" id="navbarResponsive">
				<ul class="navbar-nav ml-auto">
					<li class="nav-item mx-0 mx-lg-1"><a class="nav-link py-3 px-0 px-lg-3 rounded js-scroll-trigger"
						href="#portfolio">분석 상세</a></li>
						
					<li class="nav-item mx-0 mx-lg-1"><a class="nav-link py-3 px-0 px-lg-3 rounded js-scroll-trigger"
						href="#about">워드 클라우드</a></li>
						
					<li class="nav-item mx-0 mx-lg-1"><a class="nav-link py-3 px-0 px-lg-3 rounded js-scroll-trigger"
						href="#contact">결과 관계 분석</a></li>
				</ul>
			</div>
		</div>
	</nav>
	<!-- Masthead-->
	<header class="masthead bg-primary text-white text-center">
		<div class="container d-flex align-items-center flex-column">
			<!-- Masthead Avatar Image-->
			<img class="masthead-avatar mb-5" src="assets/img/logo.png" alt="..." />
			<!-- Masthead Heading-->
			<h1 class="masthead-heading text-uppercase mb-0">이미지를 띄울 곳.</h1>
			<!-- Icon Divider-->
			<div class="divider-custom divider-light">
				<div class="divider-custom-line"></div>
				<div class="divider-custom-icon">
					<i class="fas fa-star"></i>
				</div>
				<div class="divider-custom-line"></div>
			</div>
			<!-- Masthead Subheading-->
			<p class="masthead-subheading font-weight-light mb-0"> 태그를 나열할 곳.<br>
			 #데일리#인친#맞팔#졸업#시켜줘#눈누난나</p>
		</div>
	</header>
	<!-- 분석상세 Section-->
	<section class="page-section portfolio" id="portfolio">
		<div class="container">
			<!-- Portfolio Section Heading-->
			<h2
				class="page-section-heading text-center text-uppercase text-secondary mb-0">분석상세</h2>
			<!-- Icon Divider-->
			<div class="divider-custom">
				<div class="divider-custom-line"></div>
			</div>
			<!-- Portfolio Grid Items-->
			<div class="row justify-content-center">
				<!-- Portfolio Item 1-->
				<div class="col-md-6 col-lg-4 mb-5">
					<div class="portfolio-item mx-auto" data-toggle="modal"
						data-target="#portfolioModal1">
						<div
							class="portfolio-item-caption d-flex align-items-center justify-content-center h-100 w-100">
							<div
								class="portfolio-item-caption-content text-center text-white">
								<i class="fas fa-plus fa-3x"></i>
							</div>
						</div>
						<img class="img-fluid" src="assets/img/portfolio/cabin.png"
							alt="..." />
					</div>
				</div>
			</div>
		</div>
	</section>
	
	<!-- 워드클라우드 Section-->
	<section class="page-section bg-primary text-white mb-0" id="about">
		<div class="container">
			<!-- 워드클라우드 Section Heading-->
			<h2
				class="page-section-heading text-center text-uppercase text-white">워드클라우드</h2>
			<!-- Icon Divider-->
			<div class="divider-custom divider-light">
				<div class="divider-custom-line"></div>
			</div>
			<!-- About Section Content-->
			
			<div class="container d-flex align-items-center flex-column">
			<img class="img-fluid" src="assets/img/cloud.png" alt="..." />
			<p>워드 클라우드 사진을 삽입할 곳 입니다요</p>
			</div>
		
			
			<!-- 워드클라우드 Section Button-->
			<div class="text-center mt-4">
				<a class="btn btn-xl btn-outline-light" href="#!"> <i class="fas fa-download mr-2"></i> 
				자세한 분석 내용
				</a>
			</div>
		</div>
		
	</section>
	
	
	<!-- 결과관계분석 Section-->
	<section class="page-section" id="contact">
		<div class="container">
			<!-- 결과관계분석 Section Heading-->
			<h2
				class="page-section-heading text-center text-uppercase text-secondary mb-0">결과관계분석</h2>
				
			<!-- Icon Divider-->
			<div class="divider-custom">
				<div class="divider-custom-line"></div>
			</div>
			
			<!-- 결과관계분석 Section detail-->
			<div class="container d-flex align-items-center flex-column">
			<img class="img-fluid" src="assets/img/nodes.png" alt="..." />
			<p>결과관계분석 사진을 삽입할 곳 입니다요</p>
			</div>
		
			
			<!-- 결과관계분석 Section Button-->
			<div class="text-center mt-4">
				<a class="btn btn-xl btn-outline-light" href="#!"> <i class="fas fa-download mr-2"></i> 
				자세한 분석 내용
				</a>
			</div>
		</div>
	</section>


	<!-- Footer-->
	<footer class="footer text-center">
		<div class="container">
			<div class="row">

				<!-- Footer Location-->
				<div class="col-lg-4 mb-5 mb-lg-0">
					<h4 class="text-uppercase mb-4">개발중입니다.</h4>
					<p class="lead mb-0">
						여기에 무엇을 넣어볼까요<br /> 룰루랄라</p>
				</div>

				<!-- Footer Social Icons-->
				<div class="col-lg-4 mb-5 mb-lg-0">
					<h4 class="text-uppercase mb-4"></h4>
					<!-- a태그 잘 보기. 이미지 어디서 끌어오는지. js를 봐야할 듯. -->
					<a class="btn btn-outline-light btn-social mx-1" href="#!"><i
						class="fab fa-fw fa-facebook-f"></i></a> <a
						class="btn btn-outline-light btn-social mx-1" href="#!"><i
						class="fab fa-fw fa-twitter"></i></a> <a
						class="btn btn-outline-light btn-social mx-1" href="#!"><i
						class="fab fa-fw fa-linkedin-in"></i></a> <a
						class="btn btn-outline-light btn-social mx-1" href="#!"><i
						class="fab fa-fw fa-dribbble"></i></a>
				</div>

				<!-- Footer About Text-->
				<div class="col-lg-4">
					<h4 class="text-uppercase mb-4">여기도 개발중이에요우</h4>
					<p class="lead mb-0">
						룰루랄라 <a href=".">Start Bootstrap</a>
					</p>
				</div>
			</div>
		</div>
	</footer>



	<!-- Copyright Section-->
	<div class="copyright py-4 text-center text-white">
		<div class="container">
			<small> Copyright &copy; TAG ME <!-- This script automatically adds the current year to your website footer-->
				<!-- (credit: https://updateyourfooter.com/)--> <script>
					document.write(new Date().getFullYear());
				</script>
			</small>
		</div>
	</div>
	<!-- Scroll to Top Button (Only visible on small and extra-small screen sizes)-->
	<div class="scroll-to-top d-lg-none position-fixed">
		<a class="js-scroll-trigger d-block text-center text-white rounded"
			href="#page-top"><i class="fa fa-chevron-up"></i></a>
	</div>
	
	
	<!-- Portfolio Modals-->
	<!-- Portfolio Modal 1-->
	<div class="portfolio-modal modal fade" id="portfolioModal1"
		tabindex="-1" role="dialog" aria-labelledby="portfolioModal1Label"
		aria-hidden="true">
		<div class="modal-dialog modal-xl" role="document">
			<div class="modal-content">
				<button class="close" type="button" data-dismiss="modal"
					aria-label="Close">
					<span aria-hidden="true"><i class="fas fa-times"></i></span>
				</button>
				<div class="modal-body text-center">
					<div class="container">
						<div class="row justify-content-center">
							<div class="col-lg-3">
								<!-- Portfolio Modal - Title-->
								<h2
									class="portfolio-modal-title text-secondary text-uppercase mb-0"
									id="portfolioModal1Label">공사중</h2>
								<!-- Icon Divider-->
								<div class="divider-custom">
									<div class="divider-custom-line"></div>
									<div class="divider-custom-icon">
										<i class="fas fa-star"></i>
									</div>
									<div class="divider-custom-line"></div>
								</div>
								<!-- Portfolio Modal - Image-->
								<img class="img-fluid rounded mb-5"
									src="assets/img/portfolio/cabin.png" alt="..." />
								<!-- Portfolio Modal - Text-->
								<p class="mb-5">이 창도 어떻게든 활용해보자.</p>
								<button class="btn btn-primary" data-dismiss="modal">
									<i class="fas fa-times fa-fw"></i> Close Window
								</button>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>

	<!-- Bootstrap core JS-->
	<script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
	<script
		src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/js/bootstrap.bundle.min.js"></script>
	<!-- Third party plugin JS-->
	<script
		src="https://cdnjs.cloudflare.com/ajax/libs/animejs/3.2.1/anime.min.js"></script>
	<!-- Contact form JS-->
	<script src="assets/mail/jqBootstrapValidation.js"></script>
	<script src="assets/mail/contact_me.js"></script>
	<!-- Core theme JS-->
	<script src="js/scripts.js"></script>
</body>
</html>
