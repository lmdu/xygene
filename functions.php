<?php

remove_action('wp_head', 'wp_enqueue_scripts', 1 ); //Javascript的调用
remove_action('wp_head', 'feed_links', 2 ); //移除feed
remove_action('wp_head', 'feed_links_extra', 3 ); //移除feed
remove_action('wp_head', 'rsd_link' ); //移除离线编辑器开放接口
remove_action('wp_head', 'wlwmanifest_link' );  //移除离线编辑器开放接口
remove_action('wp_head', 'index_rel_link' );//去除本页唯一链接信息
remove_action('wp_head', 'parent_post_rel_link', 10, 0 );//清除前后文信息
remove_action('wp_head', 'start_post_rel_link', 10, 0 );//清除前后文信息
remove_action('wp_head', 'adjacent_posts_rel_link_wp_head', 10, 0 );
remove_action('wp_head', 'locale_stylesheet' );
remove_action('wp_head', 'noindex', 1 );
remove_action('wp_head', 'wp_print_styles', 8 );//载入css
remove_action('wp_head', 'wp_print_head_scripts', 9 );
remove_action('wp_head', 'wp_generator' ); //移除WordPress版本
remove_action('wp_head', 'rel_canonical' );
remove_action('wp_head', 'wp_shortlink_wp_head', 10, 0 );

remove_action('wp_footer', 'wp_print_footer_scripts' );
remove_action('template_redirect', 'wp_shortlink_header', 11, 0 );
remove_action('publish_future_post','check_and_publish_future_post',10, 1 );

remove_action('admin_print_scripts', 'print_emoji_detection_script');
remove_action('admin_print_styles', 'print_emoji_styles');
remove_action('wp_head', 'print_emoji_detection_script',	7);
remove_action('wp_print_styles', 'print_emoji_styles');
remove_action('embed_head', 'print_emoji_detection_script');
remove_filter('the_content_feed', 'wp_staticize_emoji');
remove_filter('comment_text_rss', 'wp_staticize_emoji');
remove_filter('wp_mail', 'wp_staticize_emoji_for_email');

remove_action('wp_head', 'rest_output_link_wp_head', 10 );
remove_action('wp_head', 'wp_oembed_add_discovery_links', 10 );

add_filter('show_admin_bar', '__return_false');


register_nav_menus(array(
	'main-menu' => '主导航菜单',
	'footer-menu' => '页脚菜单'
));

class description_walker extends Walker_Nav_Menu {
	function start_el(&$output, $item, $depth, $args) {
		global $wp_query;
		$indent = ( $depth ) ? str_repeat( "\t", $depth ) : '';
 
		$class_names = $value = '';
 
		$classes = empty( $item->classes ) ? array() : (array) $item->classes;
 
		$class_names = join( ' ', apply_filters( 'nav_menu_css_class', array_filter( $classes ), $item ) );
		$class_names = ' class="'. esc_attr( $class_names ) . '"';
 
		$output .= $indent . '<li id="menu-item-'. $item->ID . '"' . $value . $class_names .'>';
 
		$attributes  = ! empty( $item->attr_title ) ? ' title="'  . esc_attr( $item->attr_title ) .'"' : '';
		$attributes .= ! empty( $item->target )     ? ' target="' . esc_attr( $item->target     ) .'"' : '';
		$attributes .= ! empty( $item->xfn )        ? ' rel="'    . esc_attr( $item->xfn        ) .'"' : '';
		$attributes .= ! empty( $item->url )        ? ' href="'   . esc_attr( $item->url        ) .'"' : '';
 
		$prepend = '<span>';
		$append = '</span>';
		$description  = ! empty( $item->description ) ? '<br><span>'.esc_attr( $item->description ).'</span>' : '';
 
		if($depth != 0)
		{
			$description = $append = $prepend = "";
		}
 
		$item_output = $args->before;
		$item_output .= '<a'. $attributes .'>';
		$item_output .= $args->link_before .$prepend.apply_filters( 'the_title', $item->title, $item->ID ).$append;
		$item_output .= $description.$args->link_after;
		$item_output .= '</a>';
		$item_output .= $args->after;

		$output .= apply_filters( 'walker_nav_menu_start_el', $item_output, $item, $depth, $args );
	}
}


?>
