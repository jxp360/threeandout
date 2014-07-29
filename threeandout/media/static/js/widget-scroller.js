




<!DOCTYPE html>
<html class="   ">
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    
    
    <title>tablesorter/js/widgets/widget-scroller.js at master · Mottie/tablesorter · GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png" />
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png" />
    <meta property="fb:app_id" content="1401488693436528"/>

      <meta content="@github" name="twitter:site" /><meta content="summary" name="twitter:card" /><meta content="Mottie/tablesorter" name="twitter:title" /><meta content="Github fork of Christian Bach&amp;#39;s tablesorter plugin + awesomeness ~" name="twitter:description" /><meta content="https://avatars0.githubusercontent.com/u/136959?s=400" name="twitter:image:src" />
<meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="https://avatars0.githubusercontent.com/u/136959?s=400" property="og:image" /><meta content="Mottie/tablesorter" property="og:title" /><meta content="https://github.com/Mottie/tablesorter" property="og:url" /><meta content="Github fork of Christian Bach&#39;s tablesorter plugin + awesomeness ~" property="og:description" />

    <link rel="assets" href="https://assets-cdn.github.com/">
    <link rel="conduit-xhr" href="https://ghconduit.com:25035">
    

    <meta name="msapplication-TileImage" content="/windows-tile.png" />
    <meta name="msapplication-TileColor" content="#ffffff" />
    <meta name="selected-link" value="repo_source" data-pjax-transient />
      <meta name="google-analytics" content="UA-3769691-2">

    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="collector-cdn.github.com" name="octolytics-script-host" /><meta content="github" name="octolytics-app-id" /><meta content="6C336E06:410B:5252C43:539E6ACD" name="octolytics-dimension-request_id" />
    

    
    
    <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico" />


    <meta content="authenticity_token" name="csrf-param" />
<meta content="aFANW+9YqK3Gt8/LRcQyAvzhJveJ6G+BOURsKc3xqkglZa0AZS5D4R+D/lJa4+02wzA8gUz4ZSA1St2khLyRbw==" name="csrf-token" />

    <link href="https://assets-cdn.github.com/assets/github-6fc7fb2a2ad956975983882a7f95b27577e851a4.css" media="all" rel="stylesheet" type="text/css" />
    <link href="https://assets-cdn.github.com/assets/github2-ade82cf93cc23c0e2691785e7976cc718fe1986f.css" media="all" rel="stylesheet" type="text/css" />
    


    <meta http-equiv="x-pjax-version" content="49eb089babbf2161e2ccf648a278c589">

      
  <meta name="description" content="Github fork of Christian Bach&#39;s tablesorter plugin + awesomeness ~" />

  <meta content="136959" name="octolytics-dimension-user_id" /><meta content="Mottie" name="octolytics-dimension-user_login" /><meta content="1938370" name="octolytics-dimension-repository_id" /><meta content="Mottie/tablesorter" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="1938370" name="octolytics-dimension-repository_network_root_id" /><meta content="Mottie/tablesorter" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/Mottie/tablesorter/commits/master.atom" rel="alternate" title="Recent Commits to tablesorter:master" type="application/atom+xml" />

  </head>


  <body class="logged_out  env-production  vis-public page-blob">
    <a href="#start-of-content" tabindex="1" class="accessibility-aid js-skip-to-content">Skip to content</a>
    <div class="wrapper">
      
      
      
      


      
      <div class="header header-logged-out">
  <div class="container clearfix">

    <a class="header-logo-wordmark" href="https://github.com/">
      <span class="mega-octicon octicon-logo-github"></span>
    </a>

    <div class="header-actions">
        <a class="button primary" href="/join">Sign up</a>
      <a class="button signin" href="/login?return_to=%2FMottie%2Ftablesorter%2Fblob%2Fmaster%2Fjs%2Fwidgets%2Fwidget-scroller.js">Sign in</a>
    </div>

    <div class="command-bar js-command-bar  in-repository">

      <ul class="top-nav">
          <li class="explore"><a href="/explore">Explore</a></li>
        <li class="features"><a href="/features">Features</a></li>
          <li class="enterprise"><a href="https://enterprise.github.com/">Enterprise</a></li>
          <li class="blog"><a href="/blog">Blog</a></li>
      </ul>
        <form accept-charset="UTF-8" action="/search" class="command-bar-form" id="top_search_form" method="get">

<div class="commandbar">
  <span class="message"></span>
  <input type="text" data-hotkey="s, /" name="q" id="js-command-bar-field" placeholder="Search or type a command" tabindex="1" autocapitalize="off"
    
    
      data-repo="Mottie/tablesorter"
      data-branch="master"
      data-sha="0d7d72d18a7746fb1fba268f083e5794f387fcef"
  >
  <div class="display hidden"></div>
</div>

    <input type="hidden" name="nwo" value="Mottie/tablesorter" />

    <div class="select-menu js-menu-container js-select-menu search-context-select-menu">
      <span class="minibutton select-menu-button js-menu-target" role="button" aria-haspopup="true">
        <span class="js-select-button">This repository</span>
      </span>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container" aria-hidden="true">
        <div class="select-menu-modal">

          <div class="select-menu-item js-navigation-item js-this-repository-navigation-item selected">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" class="js-search-this-repository" name="search_target" value="repository" checked="checked" />
            <div class="select-menu-item-text js-select-button-text">This repository</div>
          </div> <!-- /.select-menu-item -->

          <div class="select-menu-item js-navigation-item js-all-repositories-navigation-item">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" name="search_target" value="global" />
            <div class="select-menu-item-text js-select-button-text">All repositories</div>
          </div> <!-- /.select-menu-item -->

        </div>
      </div>
    </div>

  <span class="help tooltipped tooltipped-s" aria-label="Show command bar help">
    <span class="octicon octicon-question"></span>
  </span>


  <input type="hidden" name="ref" value="cmdform">

</form>
    </div>

  </div>
</div>



      <div id="start-of-content" class="accessibility-aid"></div>
          <div class="site" itemscope itemtype="http://schema.org/WebPage">
    <div id="js-flash-container">
      
    </div>
    <div class="pagehead repohead instapaper_ignore readability-menu">
      <div class="container">
        

<ul class="pagehead-actions">


  <li>
    <a href="/login?return_to=%2FMottie%2Ftablesorter"
    class="minibutton with-count star-button tooltipped tooltipped-n"
    aria-label="You must be signed in to star a repository" rel="nofollow">
    <span class="octicon octicon-star"></span>Star
  </a>

    <a class="social-count js-social-count" href="/Mottie/tablesorter/stargazers">
      932
    </a>

  </li>

    <li>
      <a href="/login?return_to=%2FMottie%2Ftablesorter"
        class="minibutton with-count js-toggler-target fork-button tooltipped tooltipped-n"
        aria-label="You must be signed in to fork a repository" rel="nofollow">
        <span class="octicon octicon-repo-forked"></span>Fork
      </a>
      <a href="/Mottie/tablesorter/network" class="social-count">
        279
      </a>
    </li>
</ul>

        <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
          <span class="repo-label"><span>public</span></span>
          <span class="mega-octicon octicon-repo"></span>
          <span class="author"><a href="/Mottie" class="url fn" itemprop="url" rel="author"><span itemprop="title">Mottie</span></a></span><!--
       --><span class="path-divider">/</span><!--
       --><strong><a href="/Mottie/tablesorter" class="js-current-repository js-repo-home-link">tablesorter</a></strong>

          <span class="page-context-loader">
            <img alt="" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
          </span>

        </h1>
      </div><!-- /.container -->
    </div><!-- /.repohead -->

    <div class="container">
      <div class="repository-with-sidebar repo-container new-discussion-timeline js-new-discussion-timeline  ">
        <div class="repository-sidebar clearfix">
            

<div class="sunken-menu vertical-right repo-nav js-repo-nav js-repository-container-pjax js-octicon-loaders">
  <div class="sunken-menu-contents">
    <ul class="sunken-menu-group">
      <li class="tooltipped tooltipped-w" aria-label="Code">
        <a href="/Mottie/tablesorter" aria-label="Code" class="selected js-selected-navigation-item sunken-menu-item" data-hotkey="g c" data-pjax="true" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /Mottie/tablesorter">
          <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

        <li class="tooltipped tooltipped-w" aria-label="Issues">
          <a href="/Mottie/tablesorter/issues" aria-label="Issues" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-hotkey="g i" data-selected-links="repo_issues /Mottie/tablesorter/issues">
            <span class="octicon octicon-issue-opened"></span> <span class="full-word">Issues</span>
            <span class='counter'>68</span>
            <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>        </li>

      <li class="tooltipped tooltipped-w" aria-label="Pull Requests">
        <a href="/Mottie/tablesorter/pulls" aria-label="Pull Requests" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-hotkey="g p" data-selected-links="repo_pulls /Mottie/tablesorter/pulls">
            <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull Requests</span>
            <span class='counter'>3</span>
            <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>


        <li class="tooltipped tooltipped-w" aria-label="Wiki">
          <a href="/Mottie/tablesorter/wiki" aria-label="Wiki" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-hotkey="g w" data-selected-links="repo_wiki /Mottie/tablesorter/wiki">
            <span class="octicon octicon-book"></span> <span class="full-word">Wiki</span>
            <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>        </li>
    </ul>
    <div class="sunken-menu-separator"></div>
    <ul class="sunken-menu-group">

      <li class="tooltipped tooltipped-w" aria-label="Pulse">
        <a href="/Mottie/tablesorter/pulse" aria-label="Pulse" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="pulse /Mottie/tablesorter/pulse">
          <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped tooltipped-w" aria-label="Graphs">
        <a href="/Mottie/tablesorter/graphs" aria-label="Graphs" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="repo_graphs repo_contributors /Mottie/tablesorter/graphs">
          <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped tooltipped-w" aria-label="Network">
        <a href="/Mottie/tablesorter/network" aria-label="Network" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-selected-links="repo_network /Mottie/tablesorter/network">
          <span class="octicon octicon-repo-forked"></span> <span class="full-word">Network</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>
    </ul>


  </div>
</div>

              <div class="only-with-full-nav">
                

  

<div class="clone-url open"
  data-protocol-type="http"
  data-url="/users/set_protocol?protocol_selector=http&amp;protocol_type=clone">
  <h3><strong>HTTPS</strong> clone URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="https://github.com/Mottie/tablesorter.git" readonly="readonly">
    <span class="url-box-clippy">
    <button aria-label="copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="https://github.com/Mottie/tablesorter.git" data-copied-hint="copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  

<div class="clone-url "
  data-protocol-type="subversion"
  data-url="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=clone">
  <h3><strong>Subversion</strong> checkout URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="https://github.com/Mottie/tablesorter" readonly="readonly">
    <span class="url-box-clippy">
    <button aria-label="copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="https://github.com/Mottie/tablesorter" data-copied-hint="copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>


<p class="clone-options">You can clone with
      <a href="#" class="js-clone-selector" data-protocol="http">HTTPS</a>
      or <a href="#" class="js-clone-selector" data-protocol="subversion">Subversion</a>.
  <a href="https://help.github.com/articles/which-remote-url-should-i-use" class="help tooltipped tooltipped-n" aria-label="Get help on which URL is right for you.">
    <span class="octicon octicon-question"></span>
  </a>
</p>



                <a href="/Mottie/tablesorter/archive/master.zip"
                   class="minibutton sidebar-button"
                   aria-label="Download Mottie/tablesorter as a zip file"
                   title="Download Mottie/tablesorter as a zip file"
                   rel="nofollow">
                  <span class="octicon octicon-cloud-download"></span>
                  Download ZIP
                </a>
              </div>
        </div><!-- /.repository-sidebar -->

        <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>
          


<a href="/Mottie/tablesorter/blob/3d2f69a2a37fce4f7ca5910ad259fbe0e55a2cac/js/widgets/widget-scroller.js" class="hidden js-permalink-shortcut" data-hotkey="y">Permalink</a>

<!-- blob contrib key: blob_contributors:v21:df1eb4d5d457ad8a0d474091e223aac6 -->

<p title="This is a placeholder element" class="js-history-link-replace hidden"></p>

<div class="file-navigation">
  

<div class="select-menu js-menu-container js-select-menu" >
  <span class="minibutton select-menu-button js-menu-target css-truncate" data-hotkey="w"
    data-master-branch="master"
    data-ref="master"
    title="master"
    role="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
    <span class="octicon octicon-git-branch"></span>
    <i>branch:</i>
    <span class="js-select-button css-truncate-target">master</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax aria-hidden="true">

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-x js-menu-close"></span>
      </div> <!-- /.select-menu-header -->

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
            </li>
          </ul>
        </div><!-- /.select-menu-tabs -->
      </div><!-- /.select-menu-filters -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/blob/development/js/widgets/widget-scroller.js"
                 data-name="development"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="development">development</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/blob/gh-pages/js/widgets/widget-scroller.js"
                 data-name="gh-pages"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="gh-pages">gh-pages</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item selected">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/blob/master/js/widgets/widget-scroller.js"
                 data-name="master"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="master">master</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/blob/working/js/widgets/widget-scroller.js"
                 data-name="working"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="working">working</a>
            </div> <!-- /.select-menu-item -->
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.17.1/js/widgets/widget-scroller.js"
                 data-name="v2.17.1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.17.1">v2.17.1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.17.0/js/widgets/widget-scroller.js"
                 data-name="v2.17.0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.17.0">v2.17.0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.16.4/js/widgets/widget-scroller.js"
                 data-name="v2.16.4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.16.4">v2.16.4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.16.3/js/widgets/widget-scroller.js"
                 data-name="v2.16.3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.16.3">v2.16.3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.16.2/js/widgets/widget-scroller.js"
                 data-name="v2.16.2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.16.2">v2.16.2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.16.1-beta/js/widgets/widget-scroller.js"
                 data-name="v2.16.1-beta"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.16.1-beta">v2.16.1-beta</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.16.1/js/widgets/widget-scroller.js"
                 data-name="v2.16.1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.16.1">v2.16.1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.16.0-beta/js/widgets/widget-scroller.js"
                 data-name="v2.16.0-beta"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.16.0-beta">v2.16.0-beta</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.16.0/js/widgets/widget-scroller.js"
                 data-name="v2.16.0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.16.0">v2.16.0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.15.14/js/widgets/widget-scroller.js"
                 data-name="v2.15.14"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.15.14">v2.15.14</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.15.13/js/widgets/widget-scroller.js"
                 data-name="v2.15.13"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.15.13">v2.15.13</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.15.12/js/widgets/widget-scroller.js"
                 data-name="v2.15.12"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.15.12">v2.15.12</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.15.10/js/widgets/widget-scroller.js"
                 data-name="v2.15.10"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.15.10">v2.15.10</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.15.9/js/widgets/widget-scroller.js"
                 data-name="v2.15.9"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.15.9">v2.15.9</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.15.8/js/widgets/widget-scroller.js"
                 data-name="v2.15.8"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.15.8">v2.15.8</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.15.7/js/widgets/widget-scroller.js"
                 data-name="v2.15.7"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.15.7">v2.15.7</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.15.6/js/widgets/widget-scroller.js"
                 data-name="v2.15.6"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.15.6">v2.15.6</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.15.5/js/widgets/widget-scroller.js"
                 data-name="v2.15.5"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.15.5">v2.15.5</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.15.4/js/widgets/widget-scroller.js"
                 data-name="v2.15.4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.15.4">v2.15.4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.15.3/js/widgets/widget-scroller.js"
                 data-name="v2.15.3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.15.3">v2.15.3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.15.2/js/widgets/widget-scroller.js"
                 data-name="v2.15.2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.15.2">v2.15.2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.15.1/js/widgets/widget-scroller.js"
                 data-name="v2.15.1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.15.1">v2.15.1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.15.0/js/widgets/widget-scroller.js"
                 data-name="v2.15.0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.15.0">v2.15.0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.14.5/js/widgets/widget-scroller.js"
                 data-name="v2.14.5"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.14.5">v2.14.5</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.14.4/js/widgets/widget-scroller.js"
                 data-name="v2.14.4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.14.4">v2.14.4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.14.3/js/widgets/widget-scroller.js"
                 data-name="v2.14.3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.14.3">v2.14.3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.14.2/js/widgets/widget-scroller.js"
                 data-name="v2.14.2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.14.2">v2.14.2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.14.1/js/widgets/widget-scroller.js"
                 data-name="v2.14.1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.14.1">v2.14.1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.14.0/js/widgets/widget-scroller.js"
                 data-name="v2.14.0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.14.0">v2.14.0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.13.3/js/widgets/widget-scroller.js"
                 data-name="v2.13.3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.13.3">v2.13.3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.13.2/js/widgets/widget-scroller.js"
                 data-name="v2.13.2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.13.2">v2.13.2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.13.1/js/widgets/widget-scroller.js"
                 data-name="v2.13.1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.13.1">v2.13.1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.13.0/js/widgets/widget-scroller.js"
                 data-name="v2.13.0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.13.0">v2.13.0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.12.0/js/widgets/widget-scroller.js"
                 data-name="v2.12.0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.12.0">v2.12.0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.11.1/js/widgets/widget-scroller.js"
                 data-name="v2.11.1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.11.1">v2.11.1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.11.0/js/widgets/widget-scroller.js"
                 data-name="v2.11.0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.11.0">v2.11.0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.10.8/js/widgets/widget-scroller.js"
                 data-name="v2.10.8"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.10.8">v2.10.8</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.10.7/js/widgets/widget-scroller.js"
                 data-name="v2.10.7"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.10.7">v2.10.7</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.10.6/js/widgets/widget-scroller.js"
                 data-name="v2.10.6"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.10.6">v2.10.6</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.10.5/js/widgets/widget-scroller.js"
                 data-name="v2.10.5"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.10.5">v2.10.5</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.10.4/js/widgets/widget-scroller.js"
                 data-name="v2.10.4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.10.4">v2.10.4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.10.3/js/widgets/widget-scroller.js"
                 data-name="v2.10.3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.10.3">v2.10.3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.10.2/js/widgets/widget-scroller.js"
                 data-name="v2.10.2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.10.2">v2.10.2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.10.1/js/widgets/widget-scroller.js"
                 data-name="v2.10.1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.10.1">v2.10.1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.10.0/js/widgets/widget-scroller.js"
                 data-name="v2.10.0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.10.0">v2.10.0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.9.1/js/widgets/widget-scroller.js"
                 data-name="v2.9.1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.9.1">v2.9.1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.9.0/js/widgets/widget-scroller.js"
                 data-name="v2.9.0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.9.0">v2.9.0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.8.2/js/widgets/widget-scroller.js"
                 data-name="v2.8.2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.8.2">v2.8.2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.8.1/js/widgets/widget-scroller.js"
                 data-name="v2.8.1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.8.1">v2.8.1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.8.0/js/widgets/widget-scroller.js"
                 data-name="v2.8.0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.8.0">v2.8.0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.7.12/js/widgets/widget-scroller.js"
                 data-name="v2.7.12"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.7.12">v2.7.12</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.7.11/js/widgets/widget-scroller.js"
                 data-name="v2.7.11"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.7.11">v2.7.11</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.7.10/js/widgets/widget-scroller.js"
                 data-name="v2.7.10"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.7.10">v2.7.10</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.7.9/js/widgets/widget-scroller.js"
                 data-name="v2.7.9"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.7.9">v2.7.9</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.7.8/js/widgets/widget-scroller.js"
                 data-name="v2.7.8"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.7.8">v2.7.8</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.7.7/js/widgets/widget-scroller.js"
                 data-name="v2.7.7"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.7.7">v2.7.7</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.7.6/js/widgets/widget-scroller.js"
                 data-name="v2.7.6"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.7.6">v2.7.6</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.7.5/js/widgets/widget-scroller.js"
                 data-name="v2.7.5"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.7.5">v2.7.5</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.7.4/js/widgets/widget-scroller.js"
                 data-name="v2.7.4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.7.4">v2.7.4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.7.3/js/widgets/widget-scroller.js"
                 data-name="v2.7.3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.7.3">v2.7.3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.7.2/js/widgets/widget-scroller.js"
                 data-name="v2.7.2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.7.2">v2.7.2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.7.1/js/widgets/widget-scroller.js"
                 data-name="v2.7.1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.7.1">v2.7.1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.7/js/widgets/widget-scroller.js"
                 data-name="v2.7"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.7">v2.7</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.6.2/js/widgets/widget-scroller.js"
                 data-name="v2.6.2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.6.2">v2.6.2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.6.1/js/widgets/widget-scroller.js"
                 data-name="v2.6.1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.6.1">v2.6.1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.6/js/widgets/widget-scroller.js"
                 data-name="v2.6"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.6">v2.6</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.5.11/js/widgets/widget-scroller.js"
                 data-name="v2.5.11"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.5.11">v2.5.11</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.5.2/js/widgets/widget-scroller.js"
                 data-name="v2.5.2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.5.2">v2.5.2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.5.1/js/widgets/widget-scroller.js"
                 data-name="v2.5.1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.5.1">v2.5.1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.5/js/widgets/widget-scroller.js"
                 data-name="v2.5"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.5">v2.5</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.4.8/js/widgets/widget-scroller.js"
                 data-name="v2.4.8"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.4.8">v2.4.8</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.4.7/js/widgets/widget-scroller.js"
                 data-name="v2.4.7"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.4.7">v2.4.7</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.4.6/js/widgets/widget-scroller.js"
                 data-name="v2.4.6"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.4.6">v2.4.6</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.4.5/js/widgets/widget-scroller.js"
                 data-name="v2.4.5"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.4.5">v2.4.5</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.4.3/js/widgets/widget-scroller.js"
                 data-name="v2.4.3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.4.3">v2.4.3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.4.1/js/widgets/widget-scroller.js"
                 data-name="v2.4.1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.4.1">v2.4.1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.4/js/widgets/widget-scroller.js"
                 data-name="v2.4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.4">v2.4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.3.11/js/widgets/widget-scroller.js"
                 data-name="v2.3.11"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.3.11">v2.3.11</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.3.10/js/widgets/widget-scroller.js"
                 data-name="v2.3.10"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.3.10">v2.3.10</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.3.9/js/widgets/widget-scroller.js"
                 data-name="v2.3.9"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.3.9">v2.3.9</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.3.8/js/widgets/widget-scroller.js"
                 data-name="v2.3.8"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.3.8">v2.3.8</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.3.7/js/widgets/widget-scroller.js"
                 data-name="v2.3.7"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.3.7">v2.3.7</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.3.6/js/widgets/widget-scroller.js"
                 data-name="v2.3.6"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.3.6">v2.3.6</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.3.5/js/widgets/widget-scroller.js"
                 data-name="v2.3.5"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.3.5">v2.3.5</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.3.4/js/widgets/widget-scroller.js"
                 data-name="v2.3.4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.3.4">v2.3.4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.3.3/js/widgets/widget-scroller.js"
                 data-name="v2.3.3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.3.3">v2.3.3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.3.2/js/widgets/widget-scroller.js"
                 data-name="v2.3.2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.3.2">v2.3.2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.3.1/js/widgets/widget-scroller.js"
                 data-name="v2.3.1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.3.1">v2.3.1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.3/js/widgets/widget-scroller.js"
                 data-name="v2.3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.3">v2.3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.2.2/js/widgets/widget-scroller.js"
                 data-name="v2.2.2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.2.2">v2.2.2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.2.1/js/widgets/widget-scroller.js"
                 data-name="v2.2.1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.2.1">v2.2.1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.2/js/widgets/widget-scroller.js"
                 data-name="v2.2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.2">v2.2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.1.20/js/widgets/widget-scroller.js"
                 data-name="v2.1.20"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.1.20">v2.1.20</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.1.19/js/widgets/widget-scroller.js"
                 data-name="v2.1.19"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.1.19">v2.1.19</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.1.18/js/widgets/widget-scroller.js"
                 data-name="v2.1.18"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.1.18">v2.1.18</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.1.17/js/widgets/widget-scroller.js"
                 data-name="v2.1.17"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.1.17">v2.1.17</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.1.16/js/widgets/widget-scroller.js"
                 data-name="v2.1.16"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.1.16">v2.1.16</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.1.15/js/widgets/widget-scroller.js"
                 data-name="v2.1.15"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.1.15">v2.1.15</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.1.14/js/widgets/widget-scroller.js"
                 data-name="v2.1.14"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.1.14">v2.1.14</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.1.13/js/widgets/widget-scroller.js"
                 data-name="v2.1.13"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.1.13">v2.1.13</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.1.12/js/widgets/widget-scroller.js"
                 data-name="v2.1.12"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.1.12">v2.1.12</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.1.11/js/widgets/widget-scroller.js"
                 data-name="v2.1.11"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.1.11">v2.1.11</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.1.10/js/widgets/widget-scroller.js"
                 data-name="v2.1.10"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.1.10">v2.1.10</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.1.9/js/widgets/widget-scroller.js"
                 data-name="v2.1.9"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.1.9">v2.1.9</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.1.8/js/widgets/widget-scroller.js"
                 data-name="v2.1.8"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.1.8">v2.1.8</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.1.7/js/widgets/widget-scroller.js"
                 data-name="v2.1.7"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.1.7">v2.1.7</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.1.6/js/widgets/widget-scroller.js"
                 data-name="v2.1.6"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.1.6">v2.1.6</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.1.5/js/widgets/widget-scroller.js"
                 data-name="v2.1.5"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.1.5">v2.1.5</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.1.4/js/widgets/widget-scroller.js"
                 data-name="v2.1.4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.1.4">v2.1.4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.1.3.1/js/widgets/widget-scroller.js"
                 data-name="v2.1.3.1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.1.3.1">v2.1.3.1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.1.3/js/widgets/widget-scroller.js"
                 data-name="v2.1.3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.1.3">v2.1.3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.1.2/js/widgets/widget-scroller.js"
                 data-name="v2.1.2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.1.2">v2.1.2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.1.1/js/widgets/widget-scroller.js"
                 data-name="v2.1.1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.1.1">v2.1.1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.1/js/widgets/widget-scroller.js"
                 data-name="v2.1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.1">v2.1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.0.31/js/widgets/widget-scroller.js"
                 data-name="v2.0.31"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.0.31">v2.0.31</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.0.30.1/js/widgets/widget-scroller.js"
                 data-name="v2.0.30.1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.0.30.1">v2.0.30.1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.0.30/js/widgets/widget-scroller.js"
                 data-name="v2.0.30"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.0.30">v2.0.30</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.0.29/js/widgets/widget-scroller.js"
                 data-name="v2.0.29"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.0.29">v2.0.29</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.0.28.1/js/widgets/widget-scroller.js"
                 data-name="v2.0.28.1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.0.28.1">v2.0.28.1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.0.28/js/widgets/widget-scroller.js"
                 data-name="v2.0.28"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.0.28">v2.0.28</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.0.27/js/widgets/widget-scroller.js"
                 data-name="v2.0.27"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.0.27">v2.0.27</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.0.26/js/widgets/widget-scroller.js"
                 data-name="v2.0.26"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.0.26">v2.0.26</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.0.25.2/js/widgets/widget-scroller.js"
                 data-name="v2.0.25.2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.0.25.2">v2.0.25.2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.0.25.1/js/widgets/widget-scroller.js"
                 data-name="v2.0.25.1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.0.25.1">v2.0.25.1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.0.25/js/widgets/widget-scroller.js"
                 data-name="v2.0.25"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.0.25">v2.0.25</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.0.24/js/widgets/widget-scroller.js"
                 data-name="v2.0.24"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.0.24">v2.0.24</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.0.23.5/js/widgets/widget-scroller.js"
                 data-name="v2.0.23.5"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.0.23.5">v2.0.23.5</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.0.23.4/js/widgets/widget-scroller.js"
                 data-name="v2.0.23.4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.0.23.4">v2.0.23.4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.0.23.3/js/widgets/widget-scroller.js"
                 data-name="v2.0.23.3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.0.23.3">v2.0.23.3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.0.23.2/js/widgets/widget-scroller.js"
                 data-name="v2.0.23.2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.0.23.2">v2.0.23.2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.0.23.1/js/widgets/widget-scroller.js"
                 data-name="v2.0.23.1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.0.23.1">v2.0.23.1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.0.23/js/widgets/widget-scroller.js"
                 data-name="v2.0.23"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.0.23">v2.0.23</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.0.22/js/widgets/widget-scroller.js"
                 data-name="v2.0.22"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.0.22">v2.0.22</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.0.21.1/js/widgets/widget-scroller.js"
                 data-name="v2.0.21.1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.0.21.1">v2.0.21.1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.0.21/js/widgets/widget-scroller.js"
                 data-name="v2.0.21"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.0.21">v2.0.21</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.0.20.1/js/widgets/widget-scroller.js"
                 data-name="v2.0.20.1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.0.20.1">v2.0.20.1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.0.20/js/widgets/widget-scroller.js"
                 data-name="v2.0.20"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.0.20">v2.0.20</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.0.19/js/widgets/widget-scroller.js"
                 data-name="v2.0.19"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.0.19">v2.0.19</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.0.18.1/js/widgets/widget-scroller.js"
                 data-name="v2.0.18.1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.0.18.1">v2.0.18.1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.0.18/js/widgets/widget-scroller.js"
                 data-name="v2.0.18"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.0.18">v2.0.18</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.0.17/js/widgets/widget-scroller.js"
                 data-name="v2.0.17"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.0.17">v2.0.17</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.0.16/js/widgets/widget-scroller.js"
                 data-name="v2.0.16"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.0.16">v2.0.16</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.0.15/js/widgets/widget-scroller.js"
                 data-name="v2.0.15"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.0.15">v2.0.15</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.0.14/js/widgets/widget-scroller.js"
                 data-name="v2.0.14"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.0.14">v2.0.14</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.0.13/js/widgets/widget-scroller.js"
                 data-name="v2.0.13"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.0.13">v2.0.13</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.0.12/js/widgets/widget-scroller.js"
                 data-name="v2.0.12"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.0.12">v2.0.12</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.0.11/js/widgets/widget-scroller.js"
                 data-name="v2.0.11"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.0.11">v2.0.11</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.0.10/js/widgets/widget-scroller.js"
                 data-name="v2.0.10"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.0.10">v2.0.10</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.0.9/js/widgets/widget-scroller.js"
                 data-name="v2.0.9"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.0.9">v2.0.9</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.0.8/js/widgets/widget-scroller.js"
                 data-name="v2.0.8"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.0.8">v2.0.8</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.0.7/js/widgets/widget-scroller.js"
                 data-name="v2.0.7"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.0.7">v2.0.7</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/v2.0.6/js/widgets/widget-scroller.js"
                 data-name="v2.0.6"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="v2.0.6">v2.0.6</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/2.15.2/js/widgets/widget-scroller.js"
                 data-name="2.15.2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="2.15.2">2.15.2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/2.9.1/js/widgets/widget-scroller.js"
                 data-name="2.9.1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="2.9.1">2.9.1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/2.8.1/js/widgets/widget-scroller.js"
                 data-name="2.8.1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="2.8.1">2.8.1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/2.3.11/js/widgets/widget-scroller.js"
                 data-name="2.3.11"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="2.3.11">2.3.11</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Mottie/tablesorter/tree/2.0.22.1/js/widgets/widget-scroller.js"
                 data-name="2.0.22.1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="2.0.22.1">2.0.22.1</a>
            </div> <!-- /.select-menu-item -->
        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

    </div> <!-- /.select-menu-modal -->
  </div> <!-- /.select-menu-modal-holder -->
</div> <!-- /.select-menu -->

  <div class="button-group right">
    <a href="/Mottie/tablesorter/find/master"
          class="js-show-file-finder minibutton empty-icon tooltipped tooltipped-s"
          data-pjax
          data-hotkey="t"
          aria-label="Quickly jump between files">
      <span class="octicon octicon-list-unordered"></span>
    </a>
    <button class="js-zeroclipboard minibutton zeroclipboard-button"
          data-clipboard-text="js/widgets/widget-scroller.js"
          aria-label="Copy to clipboard"
          data-copied-hint="Copied!">
      <span class="octicon octicon-clippy"></span>
    </button>
  </div>

  <div class="breadcrumb">
    <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/Mottie/tablesorter" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">tablesorter</span></a></span></span><span class="separator"> / </span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/Mottie/tablesorter/tree/master/js" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">js</span></a></span><span class="separator"> / </span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/Mottie/tablesorter/tree/master/js/widgets" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">widgets</span></a></span><span class="separator"> / </span><strong class="final-path">widget-scroller.js</strong>
  </div>
</div>


  <div class="commit commit-loader file-history-tease js-deferred-content" data-url="/Mottie/tablesorter/contributors/master/js/widgets/widget-scroller.js">
    Fetching contributors…

    <div class="participation">
      <p class="loader-loading"><img alt="" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32-EAF2F5.gif" width="16" /></p>
      <p class="loader-error">Cannot retrieve contributors at this time</p>
    </div>
  </div>

<div class="file-box">
  <div class="file">
    <div class="meta clearfix">
      <div class="info file-name">
        <span class="icon"><b class="octicon octicon-file-text"></b></span>
        <span class="mode" title="File Mode">file</span>
        <span class="meta-divider"></span>
          <span>199 lines (164 sloc)</span>
          <span class="meta-divider"></span>
        <span>6.392 kb</span>
      </div>
      <div class="actions">
        <div class="button-group">
              <a class="minibutton disabled tooltipped tooltipped-w" href="#"
                 aria-label="You must be signed in to make or propose changes">Edit</a>
          <a href="/Mottie/tablesorter/raw/master/js/widgets/widget-scroller.js" class="button minibutton " id="raw-url">Raw</a>
            <a href="/Mottie/tablesorter/blame/master/js/widgets/widget-scroller.js" class="button minibutton js-update-url-with-hash">Blame</a>
          <a href="/Mottie/tablesorter/commits/master/js/widgets/widget-scroller.js" class="button minibutton " rel="nofollow">History</a>
        </div><!-- /.button-group -->
          <a class="minibutton danger disabled empty-icon tooltipped tooltipped-w" href="#"
             aria-label="You must be signed in to make or propose changes">
          Delete
        </a>
      </div><!-- /.actions -->
    </div>
      
  <div class="blob-wrapper data type-javascript js-blob-data">
       <table class="file-code file-diff tab-size-8">
         <tr class="file-code-line">
           <td class="blob-line-nums">
             <span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>
<span id="L58" rel="#L58">58</span>
<span id="L59" rel="#L59">59</span>
<span id="L60" rel="#L60">60</span>
<span id="L61" rel="#L61">61</span>
<span id="L62" rel="#L62">62</span>
<span id="L63" rel="#L63">63</span>
<span id="L64" rel="#L64">64</span>
<span id="L65" rel="#L65">65</span>
<span id="L66" rel="#L66">66</span>
<span id="L67" rel="#L67">67</span>
<span id="L68" rel="#L68">68</span>
<span id="L69" rel="#L69">69</span>
<span id="L70" rel="#L70">70</span>
<span id="L71" rel="#L71">71</span>
<span id="L72" rel="#L72">72</span>
<span id="L73" rel="#L73">73</span>
<span id="L74" rel="#L74">74</span>
<span id="L75" rel="#L75">75</span>
<span id="L76" rel="#L76">76</span>
<span id="L77" rel="#L77">77</span>
<span id="L78" rel="#L78">78</span>
<span id="L79" rel="#L79">79</span>
<span id="L80" rel="#L80">80</span>
<span id="L81" rel="#L81">81</span>
<span id="L82" rel="#L82">82</span>
<span id="L83" rel="#L83">83</span>
<span id="L84" rel="#L84">84</span>
<span id="L85" rel="#L85">85</span>
<span id="L86" rel="#L86">86</span>
<span id="L87" rel="#L87">87</span>
<span id="L88" rel="#L88">88</span>
<span id="L89" rel="#L89">89</span>
<span id="L90" rel="#L90">90</span>
<span id="L91" rel="#L91">91</span>
<span id="L92" rel="#L92">92</span>
<span id="L93" rel="#L93">93</span>
<span id="L94" rel="#L94">94</span>
<span id="L95" rel="#L95">95</span>
<span id="L96" rel="#L96">96</span>
<span id="L97" rel="#L97">97</span>
<span id="L98" rel="#L98">98</span>
<span id="L99" rel="#L99">99</span>
<span id="L100" rel="#L100">100</span>
<span id="L101" rel="#L101">101</span>
<span id="L102" rel="#L102">102</span>
<span id="L103" rel="#L103">103</span>
<span id="L104" rel="#L104">104</span>
<span id="L105" rel="#L105">105</span>
<span id="L106" rel="#L106">106</span>
<span id="L107" rel="#L107">107</span>
<span id="L108" rel="#L108">108</span>
<span id="L109" rel="#L109">109</span>
<span id="L110" rel="#L110">110</span>
<span id="L111" rel="#L111">111</span>
<span id="L112" rel="#L112">112</span>
<span id="L113" rel="#L113">113</span>
<span id="L114" rel="#L114">114</span>
<span id="L115" rel="#L115">115</span>
<span id="L116" rel="#L116">116</span>
<span id="L117" rel="#L117">117</span>
<span id="L118" rel="#L118">118</span>
<span id="L119" rel="#L119">119</span>
<span id="L120" rel="#L120">120</span>
<span id="L121" rel="#L121">121</span>
<span id="L122" rel="#L122">122</span>
<span id="L123" rel="#L123">123</span>
<span id="L124" rel="#L124">124</span>
<span id="L125" rel="#L125">125</span>
<span id="L126" rel="#L126">126</span>
<span id="L127" rel="#L127">127</span>
<span id="L128" rel="#L128">128</span>
<span id="L129" rel="#L129">129</span>
<span id="L130" rel="#L130">130</span>
<span id="L131" rel="#L131">131</span>
<span id="L132" rel="#L132">132</span>
<span id="L133" rel="#L133">133</span>
<span id="L134" rel="#L134">134</span>
<span id="L135" rel="#L135">135</span>
<span id="L136" rel="#L136">136</span>
<span id="L137" rel="#L137">137</span>
<span id="L138" rel="#L138">138</span>
<span id="L139" rel="#L139">139</span>
<span id="L140" rel="#L140">140</span>
<span id="L141" rel="#L141">141</span>
<span id="L142" rel="#L142">142</span>
<span id="L143" rel="#L143">143</span>
<span id="L144" rel="#L144">144</span>
<span id="L145" rel="#L145">145</span>
<span id="L146" rel="#L146">146</span>
<span id="L147" rel="#L147">147</span>
<span id="L148" rel="#L148">148</span>
<span id="L149" rel="#L149">149</span>
<span id="L150" rel="#L150">150</span>
<span id="L151" rel="#L151">151</span>
<span id="L152" rel="#L152">152</span>
<span id="L153" rel="#L153">153</span>
<span id="L154" rel="#L154">154</span>
<span id="L155" rel="#L155">155</span>
<span id="L156" rel="#L156">156</span>
<span id="L157" rel="#L157">157</span>
<span id="L158" rel="#L158">158</span>
<span id="L159" rel="#L159">159</span>
<span id="L160" rel="#L160">160</span>
<span id="L161" rel="#L161">161</span>
<span id="L162" rel="#L162">162</span>
<span id="L163" rel="#L163">163</span>
<span id="L164" rel="#L164">164</span>
<span id="L165" rel="#L165">165</span>
<span id="L166" rel="#L166">166</span>
<span id="L167" rel="#L167">167</span>
<span id="L168" rel="#L168">168</span>
<span id="L169" rel="#L169">169</span>
<span id="L170" rel="#L170">170</span>
<span id="L171" rel="#L171">171</span>
<span id="L172" rel="#L172">172</span>
<span id="L173" rel="#L173">173</span>
<span id="L174" rel="#L174">174</span>
<span id="L175" rel="#L175">175</span>
<span id="L176" rel="#L176">176</span>
<span id="L177" rel="#L177">177</span>
<span id="L178" rel="#L178">178</span>
<span id="L179" rel="#L179">179</span>
<span id="L180" rel="#L180">180</span>
<span id="L181" rel="#L181">181</span>
<span id="L182" rel="#L182">182</span>
<span id="L183" rel="#L183">183</span>
<span id="L184" rel="#L184">184</span>
<span id="L185" rel="#L185">185</span>
<span id="L186" rel="#L186">186</span>
<span id="L187" rel="#L187">187</span>
<span id="L188" rel="#L188">188</span>
<span id="L189" rel="#L189">189</span>
<span id="L190" rel="#L190">190</span>
<span id="L191" rel="#L191">191</span>
<span id="L192" rel="#L192">192</span>
<span id="L193" rel="#L193">193</span>
<span id="L194" rel="#L194">194</span>
<span id="L195" rel="#L195">195</span>
<span id="L196" rel="#L196">196</span>
<span id="L197" rel="#L197">197</span>
<span id="L198" rel="#L198">198</span>

           </td>
           <td class="blob-line-code"><div class="code-body highlight"><pre><div class='line' id='LC1'><span class="cm">/*!</span></div><div class='line' id='LC2'><span class="cm">	Copyright (C) 2011 T. Connell &amp; Associates, Inc.</span></div><div class='line' id='LC3'><br/></div><div class='line' id='LC4'><span class="cm">	Dual-licensed under the MIT and GPL licenses</span></div><div class='line' id='LC5'><br/></div><div class='line' id='LC6'><span class="cm">	THE SOFTWARE IS PROVIDED &quot;AS IS&quot;, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF</span></div><div class='line' id='LC7'><span class="cm">	MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE</span></div><div class='line' id='LC8'><span class="cm">	FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION</span></div><div class='line' id='LC9'><span class="cm">	WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.</span></div><div class='line' id='LC10'><br/></div><div class='line' id='LC11'><span class="cm">	Resizable scroller widget for the jQuery tablesorter plugin</span></div><div class='line' id='LC12'><br/></div><div class='line' id='LC13'><span class="cm">	Version 2.0 - modified by Rob Garrison 4/12/2013; updated 5/22/2014 (v2.17.0)</span></div><div class='line' id='LC14'><span class="cm">	Requires jQuery v1.7+</span></div><div class='line' id='LC15'><span class="cm">	Requires the tablesorter plugin, v2.8+, available at http://mottie.github.com/tablesorter/docs/</span></div><div class='line' id='LC16'><br/></div><div class='line' id='LC17'><span class="cm">	Usage:</span></div><div class='line' id='LC18'><br/></div><div class='line' id='LC19'><span class="cm">		$(function() {</span></div><div class='line' id='LC20'><br/></div><div class='line' id='LC21'><span class="cm">			$(&#39;table.tablesorter&#39;).tablesorter({</span></div><div class='line' id='LC22'><span class="cm">				widgets: [&#39;zebra&#39;, &#39;scroller&#39;],</span></div><div class='line' id='LC23'><span class="cm">				widgetOptions : {</span></div><div class='line' id='LC24'><span class="cm">					scroller_height       : 300,  // height of scroll window</span></div><div class='line' id='LC25'><span class="cm">					scroller_barWidth     : 17,   // scroll bar width</span></div><div class='line' id='LC26'><span class="cm">					scroller_jumpToHeader : true, // header snap to browser top when scrolling the tbody</span></div><div class='line' id='LC27'><span class="cm">					scroller_idPrefix     : &#39;s_&#39;  // cloned thead id prefix (random number added to end)</span></div><div class='line' id='LC28'><span class="cm">				}</span></div><div class='line' id='LC29'><span class="cm">			});</span></div><div class='line' id='LC30'><br/></div><div class='line' id='LC31'><span class="cm">		});</span></div><div class='line' id='LC32'><br/></div><div class='line' id='LC33'><span class="cm">	Website: www.tconnell.com</span></div><div class='line' id='LC34'><span class="cm">*/</span></div><div class='line' id='LC35'><span class="cm">/*jshint browser:true, jquery:true, unused:false */</span></div><div class='line' id='LC36'><span class="p">;(</span><span class="kd">function</span><span class="p">(</span><span class="nx">$</span><span class="p">){</span></div><div class='line' id='LC37'><span class="s2">&quot;use strict&quot;</span><span class="p">;</span></div><div class='line' id='LC38'><br/></div><div class='line' id='LC39'><span class="nx">$</span><span class="p">.</span><span class="nx">fn</span><span class="p">.</span><span class="nx">hasScrollBar</span> <span class="o">=</span> <span class="kd">function</span><span class="p">(){</span></div><div class='line' id='LC40'>	<span class="k">return</span> <span class="k">this</span><span class="p">.</span><span class="nx">get</span><span class="p">(</span><span class="mi">0</span><span class="p">).</span><span class="nx">scrollHeight</span> <span class="o">&gt;</span> <span class="k">this</span><span class="p">.</span><span class="nx">height</span><span class="p">();</span></div><div class='line' id='LC41'><span class="p">};</span></div><div class='line' id='LC42'><span class="kd">var</span> <span class="nx">ts</span> <span class="o">=</span> <span class="nx">$</span><span class="p">.</span><span class="nx">tablesorter</span><span class="p">;</span></div><div class='line' id='LC43'><br/></div><div class='line' id='LC44'><span class="nx">ts</span><span class="p">.</span><span class="nx">window_resize</span> <span class="o">=</span> <span class="kd">function</span><span class="p">(){</span></div><div class='line' id='LC45'>	<span class="k">if</span> <span class="p">(</span><span class="k">this</span><span class="p">.</span><span class="nx">resize_timer</span><span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC46'>		<span class="nx">clearTimeout</span><span class="p">(</span><span class="k">this</span><span class="p">.</span><span class="nx">resize_timer</span><span class="p">);</span> </div><div class='line' id='LC47'>	<span class="p">}</span></div><div class='line' id='LC48'>	<span class="k">this</span><span class="p">.</span><span class="nx">resize_timer</span> <span class="o">=</span> <span class="nx">setTimeout</span><span class="p">(</span><span class="kd">function</span><span class="p">(){</span></div><div class='line' id='LC49'>		<span class="nx">$</span><span class="p">(</span><span class="k">this</span><span class="p">).</span><span class="nx">trigger</span><span class="p">(</span><span class="s1">&#39;resizeEnd&#39;</span><span class="p">);</span></div><div class='line' id='LC50'>	<span class="p">},</span> <span class="mi">250</span><span class="p">);</span></div><div class='line' id='LC51'><span class="p">};</span></div><div class='line' id='LC52'><br/></div><div class='line' id='LC53'><span class="c1">// Add extra scroller css</span></div><div class='line' id='LC54'><span class="nx">$</span><span class="p">(</span><span class="kd">function</span><span class="p">(){</span></div><div class='line' id='LC55'>	<span class="kd">var</span> <span class="nx">s</span> <span class="o">=</span> <span class="s1">&#39;&lt;style&gt;&#39;</span> <span class="o">+</span></div><div class='line' id='LC56'>		<span class="s1">&#39;.tablesorter-scroller-header table.tablesorter { margin-bottom: 0; }&#39;</span> <span class="o">+</span></div><div class='line' id='LC57'>		<span class="s1">&#39;.tablesorter-scroller-table table.tablesorter { margin-top: 0; } &#39;</span> <span class="o">+</span> </div><div class='line' id='LC58'>		<span class="s1">&#39;.tablesorter-scroller-table .tablesorter-filter-row, .tablesorter-scroller-table tfoot { display: none; }&#39;</span> <span class="o">+</span></div><div class='line' id='LC59'>		<span class="s1">&#39;.tablesorter-scroller-table table.tablesorter thead tr.tablesorter-headerRow * {&#39;</span> <span class="o">+</span></div><div class='line' id='LC60'>			<span class="s1">&#39;line-height:0;height:0;border:none;background-image:none;padding-top:0;padding-bottom:0;margin-top:0;margin-bottom:0;overflow:hidden;&#39;</span> <span class="o">+</span></div><div class='line' id='LC61'>		<span class="s1">&#39;}&lt;/style&gt;&#39;</span><span class="p">;</span></div><div class='line' id='LC62'>	<span class="nx">$</span><span class="p">(</span><span class="nx">s</span><span class="p">).</span><span class="nx">appendTo</span><span class="p">(</span><span class="s1">&#39;body&#39;</span><span class="p">);</span></div><div class='line' id='LC63'><span class="p">});</span></div><div class='line' id='LC64'><br/></div><div class='line' id='LC65'><span class="nx">ts</span><span class="p">.</span><span class="nx">addWidget</span><span class="p">({</span></div><div class='line' id='LC66'>	<span class="nx">id</span><span class="o">:</span> <span class="s1">&#39;scroller&#39;</span><span class="p">,</span></div><div class='line' id='LC67'>	<span class="nx">priority</span><span class="o">:</span> <span class="mi">60</span><span class="p">,</span> <span class="c1">// run after the filter widget</span></div><div class='line' id='LC68'>	<span class="nx">options</span><span class="o">:</span> <span class="p">{</span></div><div class='line' id='LC69'>		<span class="nx">scroller_height</span> <span class="o">:</span> <span class="mi">300</span><span class="p">,</span></div><div class='line' id='LC70'>		<span class="nx">scroller_barWidth</span> <span class="o">:</span> <span class="mi">17</span><span class="p">,</span></div><div class='line' id='LC71'>		<span class="nx">scroller_jumpToHeader</span><span class="o">:</span> <span class="kc">true</span><span class="p">,</span></div><div class='line' id='LC72'>		<span class="nx">scroller_idPrefix</span> <span class="o">:</span> <span class="s1">&#39;s_&#39;</span></div><div class='line' id='LC73'>	<span class="p">},</span></div><div class='line' id='LC74'>	<span class="nx">init</span><span class="o">:</span> <span class="kd">function</span><span class="p">(</span><span class="nx">table</span><span class="p">,</span> <span class="nx">thisWidget</span><span class="p">,</span> <span class="nx">c</span><span class="p">,</span> <span class="nx">wo</span><span class="p">){</span></div><div class='line' id='LC75'>		<span class="kd">var</span> <span class="nx">$win</span> <span class="o">=</span> <span class="nx">$</span><span class="p">(</span><span class="nb">window</span><span class="p">);</span></div><div class='line' id='LC76'>		<span class="c1">//Setup window.resizeEnd event</span></div><div class='line' id='LC77'>		<span class="nx">$win</span></div><div class='line' id='LC78'>			<span class="p">.</span><span class="nx">bind</span><span class="p">(</span><span class="s1">&#39;resize&#39;</span><span class="p">,</span> <span class="nx">ts</span><span class="p">.</span><span class="nx">window_resize</span><span class="p">)</span></div><div class='line' id='LC79'>			<span class="p">.</span><span class="nx">bind</span><span class="p">(</span><span class="s1">&#39;resizeEnd&#39;</span><span class="p">,</span> <span class="kd">function</span><span class="p">()</span> <span class="p">{</span></div><div class='line' id='LC80'>				<span class="c1">// init is run before format, so scroller_resizeWidth</span></div><div class='line' id='LC81'>				<span class="c1">// won&#39;t be defined within the &quot;c&quot; or &quot;wo&quot; parameters</span></div><div class='line' id='LC82'>				<span class="k">if</span> <span class="p">(</span><span class="k">typeof</span> <span class="nx">table</span><span class="p">.</span><span class="nx">config</span><span class="p">.</span><span class="nx">widgetOptions</span><span class="p">.</span><span class="nx">scroller_resizeWidth</span> <span class="o">===</span> <span class="s1">&#39;function&#39;</span><span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC83'>					<span class="c1">//IE calls resize when you modify content, so we have to unbind the resize event</span></div><div class='line' id='LC84'>					<span class="c1">//so we don&#39;t end up with an infinite loop. we can rebind after we&#39;re done.</span></div><div class='line' id='LC85'>					<span class="nx">$win</span><span class="p">.</span><span class="nx">unbind</span><span class="p">(</span><span class="s1">&#39;resize&#39;</span><span class="p">,</span> <span class="nx">ts</span><span class="p">.</span><span class="nx">window_resize</span><span class="p">);</span></div><div class='line' id='LC86'>					<span class="nx">table</span><span class="p">.</span><span class="nx">config</span><span class="p">.</span><span class="nx">widgetOptions</span><span class="p">.</span><span class="nx">scroller_resizeWidth</span><span class="p">();</span></div><div class='line' id='LC87'>					<span class="nx">$win</span><span class="p">.</span><span class="nx">bind</span><span class="p">(</span><span class="s1">&#39;resize&#39;</span><span class="p">,</span> <span class="nx">ts</span><span class="p">.</span><span class="nx">window_resize</span><span class="p">);</span></div><div class='line' id='LC88'>				<span class="p">}</span></div><div class='line' id='LC89'>			<span class="p">});</span></div><div class='line' id='LC90'>	<span class="p">},</span></div><div class='line' id='LC91'>	<span class="nx">format</span><span class="o">:</span> <span class="kd">function</span><span class="p">(</span><span class="nx">table</span><span class="p">,</span> <span class="nx">c</span><span class="p">,</span> <span class="nx">wo</span><span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC92'>		<span class="kd">var</span> <span class="nx">h</span><span class="p">,</span> <span class="nx">$hdr</span><span class="p">,</span> <span class="nx">id</span><span class="p">,</span> <span class="nx">t</span><span class="p">,</span> <span class="nx">resize</span><span class="p">,</span> <span class="nx">$cells</span><span class="p">,</span></div><div class='line' id='LC93'>			<span class="nx">$win</span> <span class="o">=</span> <span class="nx">$</span><span class="p">(</span><span class="nb">window</span><span class="p">),</span></div><div class='line' id='LC94'>			<span class="nx">$tbl</span> <span class="o">=</span> <span class="nx">c</span><span class="p">.</span><span class="nx">$table</span><span class="p">;</span></div><div class='line' id='LC95'><br/></div><div class='line' id='LC96'>		<span class="k">if</span> <span class="p">(</span><span class="o">!</span><span class="nx">c</span><span class="p">.</span><span class="nx">isScrolling</span><span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC97'>			<span class="nx">h</span> <span class="o">=</span> <span class="nx">wo</span><span class="p">.</span><span class="nx">scroller_height</span> <span class="o">||</span> <span class="mi">300</span><span class="p">;</span></div><div class='line' id='LC98'>			<span class="nx">t</span> <span class="o">=</span> <span class="nx">$tbl</span><span class="p">.</span><span class="nx">find</span><span class="p">(</span><span class="s1">&#39;tbody&#39;</span><span class="p">).</span><span class="nx">height</span><span class="p">();</span></div><div class='line' id='LC99'>			<span class="k">if</span> <span class="p">(</span><span class="nx">t</span> <span class="o">!==</span> <span class="mi">0</span> <span class="o">&amp;&amp;</span> <span class="nx">h</span> <span class="o">&gt;</span> <span class="nx">t</span><span class="p">)</span> <span class="p">{</span> <span class="nx">h</span> <span class="o">=</span> <span class="nx">t</span> <span class="o">+</span> <span class="mi">10</span><span class="p">;</span> <span class="p">}</span>  <span class="c1">// Table is less than h px</span></div><div class='line' id='LC100'>			<span class="nx">id</span> <span class="o">=</span> <span class="nx">wo</span><span class="p">.</span><span class="nx">scroller_id</span> <span class="o">=</span> <span class="nx">wo</span><span class="p">.</span><span class="nx">scroller_idPrefix</span> <span class="o">+</span> <span class="nb">Math</span><span class="p">.</span><span class="nx">floor</span><span class="p">(</span><span class="nb">Math</span><span class="p">.</span><span class="nx">random</span><span class="p">()</span> <span class="o">*</span> <span class="mi">101</span><span class="p">);</span></div><div class='line' id='LC101'><br/></div><div class='line' id='LC102'>			<span class="nx">$hdr</span> <span class="o">=</span> <span class="nx">$</span><span class="p">(</span><span class="s1">&#39;&lt;table class=&quot;&#39;</span> <span class="o">+</span> <span class="nx">$tbl</span><span class="p">.</span><span class="nx">attr</span><span class="p">(</span><span class="s1">&#39;class&#39;</span><span class="p">)</span> <span class="o">+</span> <span class="s1">&#39;&quot; cellpadding=0 cellspacing=0&gt;&lt;thead&gt;&#39;</span> <span class="o">+</span> <span class="nx">$tbl</span><span class="p">.</span><span class="nx">find</span><span class="p">(</span><span class="s1">&#39;thead:first&#39;</span><span class="p">).</span><span class="nx">html</span><span class="p">()</span> <span class="o">+</span> <span class="s1">&#39;&lt;/thead&gt;&lt;/table&gt;&#39;</span><span class="p">);</span></div><div class='line' id='LC103'>			<span class="nx">$tbl</span></div><div class='line' id='LC104'>				<span class="p">.</span><span class="nx">wrap</span><span class="p">(</span><span class="s1">&#39;&lt;div id=&quot;&#39;</span> <span class="o">+</span> <span class="nx">id</span> <span class="o">+</span> <span class="s1">&#39;&quot; class=&quot;tablesorter-scroller&quot; style=&quot;text-align:left;&quot; /&gt;&#39;</span><span class="p">)</span></div><div class='line' id='LC105'>				<span class="p">.</span><span class="nx">before</span><span class="p">(</span><span class="nx">$hdr</span><span class="p">)</span></div><div class='line' id='LC106'>				<span class="p">.</span><span class="nx">find</span><span class="p">(</span><span class="s1">&#39;.tablesorter-filter-row&#39;</span><span class="p">).</span><span class="nx">addClass</span><span class="p">(</span><span class="s1">&#39;hideme&#39;</span><span class="p">);</span></div><div class='line' id='LC107'><br/></div><div class='line' id='LC108'>			<span class="nx">$cells</span> <span class="o">=</span> <span class="nx">$hdr</span></div><div class='line' id='LC109'>				<span class="p">.</span><span class="nx">wrap</span><span class="p">(</span><span class="s1">&#39;&lt;div class=&quot;tablesorter-scroller-header&quot; style=&quot;width:&#39;</span> <span class="o">+</span> <span class="nx">$tbl</span><span class="p">.</span><span class="nx">width</span><span class="p">()</span> <span class="o">+</span> <span class="s1">&#39;;&quot; /&gt;&#39;</span><span class="p">)</span></div><div class='line' id='LC110'>				<span class="p">.</span><span class="nx">find</span><span class="p">(</span><span class="s1">&#39;.&#39;</span> <span class="o">+</span> <span class="nx">ts</span><span class="p">.</span><span class="nx">css</span><span class="p">.</span><span class="nx">header</span><span class="p">);</span></div><div class='line' id='LC111'><br/></div><div class='line' id='LC112'>			<span class="nx">$tbl</span><span class="p">.</span><span class="nx">wrap</span><span class="p">(</span><span class="s1">&#39;&lt;div class=&quot;tablesorter-scroller-table&quot; style=&quot;height:&#39;</span> <span class="o">+</span> <span class="nx">h</span> <span class="o">+</span> <span class="s1">&#39;px;width:&#39;</span> <span class="o">+</span> <span class="nx">$tbl</span><span class="p">.</span><span class="nx">width</span><span class="p">()</span> <span class="o">+</span> <span class="s1">&#39;;overflow-y:scroll;&quot; /&gt;&#39;</span><span class="p">);</span></div><div class='line' id='LC113'><br/></div><div class='line' id='LC114'>			<span class="c1">// make scroller header sortable</span></div><div class='line' id='LC115'>			<span class="nx">ts</span><span class="p">.</span><span class="nx">bindEvents</span><span class="p">(</span><span class="nx">table</span><span class="p">,</span> <span class="nx">$cells</span><span class="p">);</span></div><div class='line' id='LC116'><br/></div><div class='line' id='LC117'>			<span class="c1">// look for filter widget</span></div><div class='line' id='LC118'>			<span class="k">if</span> <span class="p">(</span><span class="nx">$tbl</span><span class="p">.</span><span class="nx">hasClass</span><span class="p">(</span><span class="s1">&#39;hasFilters&#39;</span><span class="p">))</span> <span class="p">{</span></div><div class='line' id='LC119'>				<span class="nx">ts</span><span class="p">.</span><span class="nx">filter</span><span class="p">.</span><span class="nx">bindSearch</span><span class="p">(</span> <span class="nx">$tbl</span><span class="p">,</span> <span class="nx">$hdr</span><span class="p">.</span><span class="nx">find</span><span class="p">(</span><span class="s1">&#39;.&#39;</span> <span class="o">+</span> <span class="nx">ts</span><span class="p">.</span><span class="nx">css</span><span class="p">.</span><span class="nx">filter</span><span class="p">)</span> <span class="p">);</span></div><div class='line' id='LC120'>			<span class="p">}</span></div><div class='line' id='LC121'><br/></div><div class='line' id='LC122'>			<span class="nx">resize</span> <span class="o">=</span> <span class="kd">function</span><span class="p">(){</span></div><div class='line' id='LC123'>				<span class="kd">var</span> <span class="nx">d</span><span class="p">,</span></div><div class='line' id='LC124'>					<span class="c1">//Hide other scrollers so we can resize</span></div><div class='line' id='LC125'>					<span class="nx">$div</span> <span class="o">=</span> <span class="nx">$</span><span class="p">(</span><span class="s1">&#39;div.scroller[id != &quot;&#39;</span> <span class="o">+</span> <span class="nx">id</span> <span class="o">+</span> <span class="s1">&#39;&quot;]&#39;</span><span class="p">).</span><span class="nx">hide</span><span class="p">();</span></div><div class='line' id='LC126'><br/></div><div class='line' id='LC127'>				<span class="nx">$tbl</span><span class="p">.</span><span class="nx">find</span><span class="p">(</span><span class="s1">&#39;thead&#39;</span><span class="p">).</span><span class="nx">show</span><span class="p">();</span></div><div class='line' id='LC128'><br/></div><div class='line' id='LC129'>				<span class="c1">//Reset sizes so parent can resize.</span></div><div class='line' id='LC130'>				<span class="nx">$hdr</span></div><div class='line' id='LC131'>					<span class="p">.</span><span class="nx">width</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span></div><div class='line' id='LC132'>					<span class="p">.</span><span class="nx">parent</span><span class="p">().</span><span class="nx">width</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span></div><div class='line' id='LC133'>					<span class="p">.</span><span class="nx">find</span><span class="p">(</span><span class="s1">&#39;th,td&#39;</span><span class="p">).</span><span class="nx">width</span><span class="p">(</span><span class="mi">0</span><span class="p">);</span></div><div class='line' id='LC134'><br/></div><div class='line' id='LC135'>				<span class="nx">$tbl</span></div><div class='line' id='LC136'>					<span class="p">.</span><span class="nx">width</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span></div><div class='line' id='LC137'>					<span class="p">.</span><span class="nx">find</span><span class="p">(</span><span class="s1">&#39;thead&#39;</span><span class="p">).</span><span class="nx">find</span><span class="p">(</span><span class="s1">&#39;th,td&#39;</span><span class="p">).</span><span class="nx">width</span><span class="p">(</span><span class="mi">0</span><span class="p">);</span></div><div class='line' id='LC138'>				<span class="nx">d</span> <span class="o">=</span> <span class="nx">$tbl</span><span class="p">.</span><span class="nx">parent</span><span class="p">();</span></div><div class='line' id='LC139'>				<span class="nx">d</span><span class="p">.</span><span class="nx">width</span><span class="p">(</span><span class="mi">0</span><span class="p">);</span></div><div class='line' id='LC140'><br/></div><div class='line' id='LC141'>				<span class="nx">d</span><span class="p">.</span><span class="nx">parent</span><span class="p">().</span><span class="nx">trigger</span><span class="p">(</span><span class="s1">&#39;resize&#39;</span><span class="p">);</span></div><div class='line' id='LC142'>				<span class="c1">// Shrink a bit to accommodate scrollbar</span></div><div class='line' id='LC143'>				<span class="nx">d</span><span class="p">.</span><span class="nx">width</span><span class="p">(</span> <span class="nx">d</span><span class="p">.</span><span class="nx">parent</span><span class="p">().</span><span class="nx">innerWidth</span><span class="p">()</span> <span class="o">-</span> <span class="p">(</span> <span class="nx">d</span><span class="p">.</span><span class="nx">parent</span><span class="p">().</span><span class="nx">hasScrollBar</span><span class="p">()</span> <span class="o">?</span> <span class="nx">wo</span><span class="p">.</span><span class="nx">scroller_barWidth</span> <span class="o">:</span> <span class="mi">0</span> <span class="p">)</span> <span class="p">);</span></div><div class='line' id='LC144'><br/></div><div class='line' id='LC145'>				<span class="nx">$tbl</span><span class="p">.</span><span class="nx">width</span><span class="p">(</span> <span class="nx">d</span><span class="p">.</span><span class="nx">innerWidth</span><span class="p">()</span> <span class="o">-</span> <span class="p">(</span> <span class="nx">d</span><span class="p">.</span><span class="nx">hasScrollBar</span><span class="p">()</span> <span class="o">?</span> <span class="nx">wo</span><span class="p">.</span><span class="nx">scroller_barWidth</span> <span class="o">:</span> <span class="mi">0</span> <span class="p">)</span> <span class="p">);</span></div><div class='line' id='LC146'>				<span class="nx">$tbl</span><span class="p">.</span><span class="nx">find</span><span class="p">(</span><span class="s1">&#39;thead&#39;</span><span class="p">).</span><span class="nx">find</span><span class="p">(</span><span class="s1">&#39;th,td&#39;</span><span class="p">).</span><span class="nx">filter</span><span class="p">(</span><span class="s1">&#39;:visible&#39;</span><span class="p">).</span><span class="nx">each</span><span class="p">(</span><span class="kd">function</span><span class="p">(</span><span class="nx">i</span><span class="p">,</span> <span class="nx">c</span><span class="p">){</span></div><div class='line' id='LC147'>					<span class="kd">var</span> <span class="nx">$th</span> <span class="o">=</span> <span class="nx">$</span><span class="p">(</span><span class="nx">c</span><span class="p">),</span></div><div class='line' id='LC148'>					<span class="c1">//Wrap in browser detect??</span></div><div class='line' id='LC149'>					<span class="nx">w</span> <span class="o">=</span> <span class="nb">parseInt</span><span class="p">(</span> <span class="nx">$th</span><span class="p">.</span><span class="nx">css</span><span class="p">(</span><span class="s1">&#39;min-width&#39;</span><span class="p">).</span><span class="nx">replace</span><span class="p">(</span><span class="s1">&#39;auto&#39;</span><span class="p">,</span> <span class="s1">&#39;0&#39;</span><span class="p">).</span><span class="nx">replace</span><span class="p">(</span><span class="sr">/(px|em)/</span><span class="p">,</span> <span class="s1">&#39;&#39;</span><span class="p">),</span> <span class="mi">10</span> <span class="p">);</span></div><div class='line' id='LC150'>					<span class="k">if</span> <span class="p">(</span> <span class="nx">$th</span><span class="p">.</span><span class="nx">width</span><span class="p">()</span> <span class="o">&lt;</span> <span class="nx">w</span> <span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC151'>						<span class="nx">$th</span><span class="p">.</span><span class="nx">width</span><span class="p">(</span><span class="nx">w</span><span class="p">);</span></div><div class='line' id='LC152'>					<span class="p">}</span> <span class="k">else</span> <span class="p">{</span></div><div class='line' id='LC153'>						<span class="nx">w</span> <span class="o">=</span> <span class="nx">$th</span><span class="p">.</span><span class="nx">width</span><span class="p">();</span></div><div class='line' id='LC154'>					<span class="p">}</span></div><div class='line' id='LC155'>					<span class="nx">$hdr</span><span class="p">.</span><span class="nx">find</span><span class="p">(</span><span class="s1">&#39;th,td&#39;</span><span class="p">).</span><span class="nx">eq</span><span class="p">(</span><span class="nx">i</span><span class="p">).</span><span class="nx">width</span><span class="p">(</span><span class="nx">w</span><span class="p">);</span></div><div class='line' id='LC156'>				<span class="p">});</span></div><div class='line' id='LC157'><br/></div><div class='line' id='LC158'>				<span class="nx">$hdr</span><span class="p">.</span><span class="nx">width</span><span class="p">(</span><span class="nx">$tbl</span><span class="p">.</span><span class="nx">innerWidth</span><span class="p">());</span></div><div class='line' id='LC159'>				<span class="nx">$div</span><span class="p">.</span><span class="nx">show</span><span class="p">();</span></div><div class='line' id='LC160'>			<span class="p">};</span></div><div class='line' id='LC161'><br/></div><div class='line' id='LC162'>			<span class="c1">//Expose to external calls</span></div><div class='line' id='LC163'>			<span class="nx">wo</span><span class="p">.</span><span class="nx">scroller_resizeWidth</span> <span class="o">=</span> <span class="nx">resize</span><span class="p">;</span></div><div class='line' id='LC164'><br/></div><div class='line' id='LC165'>			<span class="nx">resize</span><span class="p">();</span></div><div class='line' id='LC166'><br/></div><div class='line' id='LC167'>			<span class="nx">$tbl</span><span class="p">.</span><span class="nx">find</span><span class="p">(</span><span class="s1">&#39;thead&#39;</span><span class="p">).</span><span class="nx">css</span><span class="p">(</span><span class="s1">&#39;visibility&#39;</span><span class="p">,</span> <span class="s1">&#39;hidden&#39;</span><span class="p">);</span></div><div class='line' id='LC168'>			<span class="nx">c</span><span class="p">.</span><span class="nx">isScrolling</span> <span class="o">=</span> <span class="kc">true</span><span class="p">;</span></div><div class='line' id='LC169'><br/></div><div class='line' id='LC170'>			<span class="nx">t</span> <span class="o">=</span> <span class="nx">$tbl</span><span class="p">.</span><span class="nx">parent</span><span class="p">().</span><span class="nx">parent</span><span class="p">().</span><span class="nx">height</span><span class="p">();</span></div><div class='line' id='LC171'>			<span class="c1">// The header will always jump into view if scrolling the table body</span></div><div class='line' id='LC172'>			<span class="nx">$tbl</span><span class="p">.</span><span class="nx">parent</span><span class="p">().</span><span class="nx">bind</span><span class="p">(</span><span class="s1">&#39;scroll&#39;</span><span class="p">,</span> <span class="kd">function</span><span class="p">(){</span></div><div class='line' id='LC173'>				<span class="k">if</span> <span class="p">(</span><span class="nx">wo</span><span class="p">.</span><span class="nx">scroller_jumpToHeader</span><span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC174'>					<span class="kd">var</span> <span class="nx">pos</span> <span class="o">=</span> <span class="nx">$win</span><span class="p">.</span><span class="nx">scrollTop</span><span class="p">()</span> <span class="o">-</span> <span class="nx">$hdr</span><span class="p">.</span><span class="nx">offset</span><span class="p">().</span><span class="nx">top</span><span class="p">;</span></div><div class='line' id='LC175'>					<span class="k">if</span> <span class="p">(</span><span class="nx">$</span><span class="p">(</span><span class="k">this</span><span class="p">).</span><span class="nx">scrollTop</span><span class="p">()</span> <span class="o">!==</span> <span class="mi">0</span> <span class="o">&amp;&amp;</span> <span class="nx">pos</span> <span class="o">&lt;</span> <span class="nx">t</span> <span class="o">&amp;&amp;</span> <span class="nx">pos</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC176'>						<span class="nx">$win</span><span class="p">.</span><span class="nx">scrollTop</span><span class="p">(</span> <span class="nx">$hdr</span><span class="p">.</span><span class="nx">offset</span><span class="p">().</span><span class="nx">top</span> <span class="p">);</span></div><div class='line' id='LC177'>					<span class="p">}</span></div><div class='line' id='LC178'>				<span class="p">}</span></div><div class='line' id='LC179'>			<span class="p">});</span></div><div class='line' id='LC180'><br/></div><div class='line' id='LC181'>		<span class="p">}</span></div><div class='line' id='LC182'><br/></div><div class='line' id='LC183'>		<span class="c1">//Sorting, so scroll to top</span></div><div class='line' id='LC184'>		<span class="nx">$tbl</span><span class="p">.</span><span class="nx">parent</span><span class="p">().</span><span class="nx">animate</span><span class="p">({</span> <span class="nx">scrollTop</span><span class="o">:</span> <span class="mi">0</span> <span class="p">},</span> <span class="s1">&#39;fast&#39;</span><span class="p">);</span></div><div class='line' id='LC185'><br/></div><div class='line' id='LC186'>	<span class="p">},</span></div><div class='line' id='LC187'>	<span class="nx">remove</span> <span class="o">:</span> <span class="kd">function</span><span class="p">(</span><span class="nx">table</span><span class="p">,</span> <span class="nx">c</span><span class="p">,</span> <span class="nx">wo</span><span class="p">){</span></div><div class='line' id='LC188'>		<span class="kd">var</span> <span class="nx">$table</span> <span class="o">=</span> <span class="nx">c</span><span class="p">.</span><span class="nx">$table</span><span class="p">;</span></div><div class='line' id='LC189'>		<span class="nx">$table</span><span class="p">.</span><span class="nx">closest</span><span class="p">(</span><span class="s1">&#39;.tablesorter-scroller&#39;</span><span class="p">).</span><span class="nx">find</span><span class="p">(</span><span class="s1">&#39;.tablesorter-scroller-header&#39;</span><span class="p">).</span><span class="nx">remove</span><span class="p">();</span></div><div class='line' id='LC190'>		<span class="nx">$table</span></div><div class='line' id='LC191'>				<span class="p">.</span><span class="nx">unwrap</span><span class="p">()</span></div><div class='line' id='LC192'>				<span class="p">.</span><span class="nx">find</span><span class="p">(</span><span class="s1">&#39;.tablesorter-filter-row&#39;</span><span class="p">).</span><span class="nx">removeClass</span><span class="p">(</span><span class="s1">&#39;hideme&#39;</span><span class="p">).</span><span class="nx">end</span><span class="p">()</span></div><div class='line' id='LC193'>				<span class="p">.</span><span class="nx">find</span><span class="p">(</span><span class="s1">&#39;thead&#39;</span><span class="p">).</span><span class="nx">show</span><span class="p">().</span><span class="nx">css</span><span class="p">(</span><span class="s1">&#39;visibility&#39;</span><span class="p">,</span> <span class="s1">&#39;visible&#39;</span><span class="p">);</span></div><div class='line' id='LC194'>		<span class="nx">c</span><span class="p">.</span><span class="nx">isScrolling</span> <span class="o">=</span> <span class="kc">false</span><span class="p">;</span></div><div class='line' id='LC195'>	<span class="p">}</span></div><div class='line' id='LC196'><span class="p">});</span></div><div class='line' id='LC197'><br/></div><div class='line' id='LC198'><span class="p">})(</span><span class="nx">jQuery</span><span class="p">);</span></div></pre></div></td>
         </tr>
       </table>
  </div>

  </div>
</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" class="js-jump-to-line" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <form accept-charset="UTF-8" class="js-jump-to-line-form">
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" autofocus>
    <button type="submit" class="button">Go</button>
  </form>
</div>

        </div>

      </div><!-- /.repo-container -->
      <div class="modal-backdrop"></div>
    </div><!-- /.container -->
  </div><!-- /.site -->


    </div><!-- /.wrapper -->

      <div class="container">
  <div class="site-footer">
    <ul class="site-footer-links right">
      <li><a href="https://status.github.com/">Status</a></li>
      <li><a href="http://developer.github.com">API</a></li>
      <li><a href="http://training.github.com">Training</a></li>
      <li><a href="http://shop.github.com">Shop</a></li>
      <li><a href="/blog">Blog</a></li>
      <li><a href="/about">About</a></li>

    </ul>

    <a href="/">
      <span class="mega-octicon octicon-mark-github" title="GitHub"></span>
    </a>

    <ul class="site-footer-links">
      <li>&copy; 2014 <span title="0.07795s from github-fe139-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="/site/terms">Terms</a></li>
        <li><a href="/site/privacy">Privacy</a></li>
        <li><a href="/security">Security</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
  </div><!-- /.site-footer -->
</div><!-- /.container -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-fullscreen-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="fullscreen-contents js-fullscreen-contents" placeholder="" data-suggester="fullscreen_suggester"></textarea>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped tooltipped-w" aria-label="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped tooltipped-w"
      aria-label="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-x close js-ajax-error-dismiss" aria-label="Dismiss error"></a>
      Something went wrong with that request. Please try again.
    </div>


      <script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/frameworks-c23f6bb20db24ab07b4ee77598ac060d1ca974e3.js" type="text/javascript"></script>
      <script async="async" crossorigin="anonymous" src="https://assets-cdn.github.com/assets/github-364e8672efe83959268c1ce088c13e3739d9d275.js" type="text/javascript"></script>
      
      
        <script async src="https://www.google-analytics.com/analytics.js"></script>
  </body>
</html>

