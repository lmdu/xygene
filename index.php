<!DOCTYPE html>
<html <?php language_attributes(); ?>>
<head>
	<meta charset="<?php bloginfo('charset'); ?>">
	<script src="<?php bloginfo('template_url'); ?>/thirds/jquery-1.12.2.min.js"></script>
	<link rel="stylesheet" href="<?php bloginfo('template_url'); ?>/thirds/semantic/semantic.min.css">
	<script src="<?php bloginfo('template_url'); ?>/thirds/semantic/semantic.min.js"></script>
	<?php if(is_home()): ?>
	<link rel="stylesheet" href="<?php bloginfo('template_url'); ?>/thirds/eslider/eslider.css">
	<script src="<?php bloginfo('template_url'); ?>/thirds/eslider/eslider.js"></script>
	<?php endif; ?>
	<link rel="stylesheet" href="<?php bloginfo('stylesheet_url'); ?>">
	<script src="<?php bloginfo('template_url'); ?>/script.js"></script>
	<title><?php bloginfo('name'); ?></title>
	<?php wp_head(); ?>
</head>
<body>
<div class="ui centered grid container">
	<div class="row">
		<div class="column"><h1 class="logo">鑫云解码</h1></div>
	</div>

	<div class="row">
	<div class="column">
		<div class="slideshow">
			<ul class="sliders">
				<li><img src="<?php bloginfo('template_url'); ?>/img/bg4.png"></li>
				<li>
					<img src="<?php bloginfo('template_url'); ?>/img/bg1.jpg">
					<div class="content">
						<div>
						<h3>DOT Navigation</h3>
						<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit,</p>
						<p>sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
						<a href="" class="slider-btn">READ MORE</a>
						</div>
					</div>
				</li>
				<li><img src="<?php bloginfo('template_url'); ?>/img/bg2.jpg"></li>
				<li><img src="<?php bloginfo('template_url'); ?>/img/bg3.jpg"></li>
			</ul>
		</div>
	</div>
	</div>
	<div class="row">
		<div class="column">
			<div class="ui horizontal bulleted link list">
			  <a class="item">关于我们</a>
			  <a class="item">联系我们</a>
			  <a class="item">检测方案</a>
			</div>
			<div class="ui right floated horizontal link list">
  				<div class="disabled item" href="#">©成都鑫云解码科技有限公司</div>
  				<a class="item" href="#">蜀ICP备16008635号</a>
  				<a class="item" href="#">隐私政策</a>
  				<a class="item" href="#">法律声明</a>
  				<a class="item" href="#">FAQ</a>
			</div>
		</div>
	</div>
</div>

</body>
</html>