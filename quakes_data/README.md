





<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">



  <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/frameworks-223154a4264e621d49411c69fd71062cb152480ce2de3bde5ae285e801db7185.css" media="all" rel="stylesheet" />
  <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/github-11c46449861d69b02a101da2d9e4232e7213635a4d2839dde7e30604f59cf718.css" media="all" rel="stylesheet" />
  
  
  <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/site-d826c765b656f31c7d808168e332aa14ccb724820f292ecd2dfb74b156e2ebde.css" media="all" rel="stylesheet" />
  

  <meta name="viewport" content="width=device-width">
  
  <title>libcomcat/README.md at master · usgs/libcomcat · GitHub</title>
  <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
  <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
  <meta property="fb:app_id" content="1401488693436528">

    
    <meta content="https://avatars1.githubusercontent.com/u/1091434?v=3&amp;s=400" property="og:image" /><meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="usgs/libcomcat" property="og:title" /><meta content="https://github.com/usgs/libcomcat" property="og:url" /><meta content="libcomcat - Library of functions and wrapper scripts for accessing NEIC ComCat server data" property="og:description" />

  <link rel="assets" href="https://assets-cdn.github.com/">
  
  <meta name="pjax-timeout" content="1000">
  
  <meta name="request-id" content="88CF:622A:2F89B63:46A2131:58F3E33F" data-pjax-transient>
  

  <meta name="selected-link" value="repo_source" data-pjax-transient>

  <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
<meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
    <meta name="google-analytics" content="UA-3769691-2">

<meta content="collector.githubapp.com" name="octolytics-host" /><meta content="github" name="octolytics-app-id" /><meta content="https://collector.githubapp.com/github-external/browser_event" name="octolytics-event-url" /><meta content="88CF:622A:2F89B63:46A2131:58F3E33F" name="octolytics-dimension-request_id" />
<meta content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-pjax-transient="true" name="analytics-location" />




  <meta class="js-ga-set" name="dimension1" content="Logged Out">


  

      <meta name="hostname" content="github.com">
  <meta name="user-login" content="">

      <meta name="expected-hostname" content="github.com">
    <meta name="js-proxy-site-detection-payload" content="MWFkZjBiNjA0YjBkYzZlYzU0ZjAyNDliNDBkYzEyYWY4NWFlMDg2NmU0ZmY5MTA3Y2JhMDk4MGY3NjNjODZmMHx7InJlbW90ZV9hZGRyZXNzIjoiMzQuMjA3LjI1MS4xNzUiLCJyZXF1ZXN0X2lkIjoiODhDRjo2MjJBOjJGODlCNjM6NDZBMjEzMTo1OEYzRTMzRiIsInRpbWVzdGFtcCI6MTQ5MjM3ODQzMSwiaG9zdCI6ImdpdGh1Yi5jb20ifQ==">


  <meta name="html-safe-nonce" content="8ef418b7a1acea81d5407855432584a062e2920e">

  <meta http-equiv="x-pjax-version" content="687002853f6963ad768d20799cfd58be">
  

    
  <meta name="description" content="libcomcat - Library of functions and wrapper scripts for accessing NEIC ComCat server data">
  <meta name="go-import" content="github.com/usgs/libcomcat git https://github.com/usgs/libcomcat.git">

  <meta content="1091434" name="octolytics-dimension-user_id" /><meta content="usgs" name="octolytics-dimension-user_login" /><meta content="11646008" name="octolytics-dimension-repository_id" /><meta content="usgs/libcomcat" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="11646008" name="octolytics-dimension-repository_network_root_id" /><meta content="usgs/libcomcat" name="octolytics-dimension-repository_network_root_nwo" />
        <link href="https://github.com/usgs/libcomcat/commits/master.atom" rel="alternate" title="Recent Commits to libcomcat:master" type="application/atom+xml">


    <link rel="canonical" href="https://github.com/usgs/libcomcat/blob/master/README.md" data-pjax-transient>


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <link rel="mask-icon" href="https://assets-cdn.github.com/pinned-octocat.svg" color="#000000">
  <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico">

<meta name="theme-color" content="#1e2327">



  </head>

  <body class="logged-out env-production page-blob">
    


  <div class="position-relative js-header-wrapper ">
    <a href="#start-of-content" tabindex="1" class="accessibility-aid js-skip-to-content">Skip to content</a>
    <div id="js-pjax-loader-bar" class="pjax-loader-bar"><div class="progress"></div></div>

    
    
    



          <header class="site-header js-details-container Details" role="banner">
  <div class="container-responsive">
    <a class="header-logo-invertocat" href="https://github.com/" aria-label="Homepage" data-ga-click="(Logged out) Header, go to homepage, icon:logo-wordmark">
      <svg aria-hidden="true" class="octicon octicon-mark-github" height="32" version="1.1" viewBox="0 0 16 16" width="32"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
    </a>

    <button class="btn-link float-right site-header-toggle js-details-target" type="button" aria-label="Toggle navigation">
      <svg aria-hidden="true" class="octicon octicon-three-bars" height="24" version="1.1" viewBox="0 0 12 16" width="18"><path fill-rule="evenodd" d="M11.41 9H.59C0 9 0 8.59 0 8c0-.59 0-1 .59-1H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1h.01zm0-4H.59C0 5 0 4.59 0 4c0-.59 0-1 .59-1H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1h.01zM.59 11H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1H.59C0 13 0 12.59 0 12c0-.59 0-1 .59-1z"/></svg>
    </button>

    <div class="site-header-menu">
      <nav class="site-header-nav">
        <a href="/features" class="js-selected-navigation-item nav-item" data-ga-click="Header, click, Nav menu - item:features" data-selected-links="/features /features">
          Features
</a>        <a href="/business" class="js-selected-navigation-item nav-item" data-ga-click="Header, click, Nav menu - item:business" data-selected-links="/business /business/security /business/customers /business">
          Business
</a>        <a href="/explore" class="js-selected-navigation-item nav-item" data-ga-click="Header, click, Nav menu - item:explore" data-selected-links="/explore /trending /trending/developers /integrations /integrations/feature/code /integrations/feature/collaborate /integrations/feature/ship /showcases /explore">
          Explore
</a>        <a href="/pricing" class="js-selected-navigation-item nav-item" data-ga-click="Header, click, Nav menu - item:pricing" data-selected-links="/pricing /pricing">
          Pricing
</a>      </nav>

      <div class="site-header-actions">
          <div class="header-search scoped-search site-scoped-search js-site-search" role="search">
  <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/usgs/libcomcat/search" class="js-site-search-form" data-scoped-search-url="/usgs/libcomcat/search" data-unscoped-search-url="/search" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
    <label class="form-control header-search-wrapper js-chromeless-input-container">
        <a href="/usgs/libcomcat/blob/master/README.md" class="header-search-scope no-underline">This repository</a>
      <input type="text"
        class="form-control header-search-input js-site-search-focus js-site-search-field is-clearable"
        data-hotkey="s"
        name="q"
        value=""
        placeholder="Search"
        aria-label="Search this repository"
        data-unscoped-placeholder="Search GitHub"
        data-scoped-placeholder="Search"
        autocapitalize="off">
        <input type="hidden" class="js-site-search-type-field" name="type" >
    </label>
</form></div>


          <a class="text-bold site-header-link" href="/login?return_to=%2Fusgs%2Flibcomcat%2Fblob%2Fmaster%2FREADME.md" data-ga-click="(Logged out) Header, clicked Sign in, text:sign-in">Sign in</a>
            <span class="text-gray">or</span>
            <a class="text-bold site-header-link" href="/join?source=header-repo" data-ga-click="(Logged out) Header, clicked Sign up, text:sign-up">Sign up</a>
      </div>
    </div>
  </div>
</header>


  </div>

  <div id="start-of-content" class="accessibility-aid"></div>

    <div id="js-flash-container">
</div>



  <div role="main">
        <div itemscope itemtype="http://schema.org/SoftwareSourceCode">
    <div id="js-repo-pjax-container" data-pjax-container>
        



  <div class="pagehead repohead instapaper_ignore readability-menu experiment-repo-nav">
    <div class="container repohead-details-container">


      <ul class="pagehead-actions">
  <li>
      <a href="/login?return_to=%2Fusgs%2Flibcomcat"
    class="btn btn-sm btn-with-count tooltipped tooltipped-n"
    aria-label="You must be signed in to watch a repository" rel="nofollow">
    <svg aria-hidden="true" class="octicon octicon-eye" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
    Watch
  </a>
  <a class="social-count" href="/usgs/libcomcat/watchers"
     aria-label="20 users are watching this repository">
    20
  </a>

  </li>

  <li>
      <a href="/login?return_to=%2Fusgs%2Flibcomcat"
    class="btn btn-sm btn-with-count tooltipped tooltipped-n"
    aria-label="You must be signed in to star a repository" rel="nofollow">
    <svg aria-hidden="true" class="octicon octicon-star" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74z"/></svg>
    Star
  </a>

    <a class="social-count js-social-count" href="/usgs/libcomcat/stargazers"
      aria-label="6 users starred this repository">
      6
    </a>

  </li>

  <li>
      <a href="/login?return_to=%2Fusgs%2Flibcomcat"
        class="btn btn-sm btn-with-count tooltipped tooltipped-n"
        aria-label="You must be signed in to fork a repository" rel="nofollow">
        <svg aria-hidden="true" class="octicon octicon-repo-forked" height="16" version="1.1" viewBox="0 0 10 16" width="10"><path fill-rule="evenodd" d="M8 1a1.993 1.993 0 0 0-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 0 0 2 1a1.993 1.993 0 0 0-1 3.72V6.5l3 3v1.78A1.993 1.993 0 0 0 5 15a1.993 1.993 0 0 0 1-3.72V9.5l3-3V4.72A1.993 1.993 0 0 0 8 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
        Fork
      </a>

    <a href="/usgs/libcomcat/network" class="social-count"
       aria-label="16 users forked this repository">
      16
    </a>
  </li>
</ul>

      <h1 class="public ">
  <svg aria-hidden="true" class="octicon octicon-repo" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
  <span class="author" itemprop="author"><a href="/usgs" class="url fn" rel="author">usgs</a></span><!--
--><span class="path-divider">/</span><!--
--><strong itemprop="name"><a href="/usgs/libcomcat" data-pjax="#js-repo-pjax-container">libcomcat</a></strong>

</h1>

    </div>
    <div class="container">
      
<nav class="reponav js-repo-nav js-sidenav-container-pjax"
     itemscope
     itemtype="http://schema.org/BreadcrumbList"
     role="navigation"
     data-pjax="#js-repo-pjax-container">

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a href="/usgs/libcomcat" class="js-selected-navigation-item selected reponav-item" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /usgs/libcomcat" itemprop="url">
      <svg aria-hidden="true" class="octicon octicon-code" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M9.5 3L8 4.5 11.5 8 8 11.5 9.5 13 14 8 9.5 3zm-5 0L0 8l4.5 5L6 11.5 2.5 8 6 4.5 4.5 3z"/></svg>
      <span itemprop="name">Code</span>
      <meta itemprop="position" content="1">
</a>  </span>

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a href="/usgs/libcomcat/issues" class="js-selected-navigation-item reponav-item" data-hotkey="g i" data-selected-links="repo_issues repo_labels repo_milestones /usgs/libcomcat/issues" itemprop="url">
        <svg aria-hidden="true" class="octicon octicon-issue-opened" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"/></svg>
        <span itemprop="name">Issues</span>
        <span class="counter">8</span>
        <meta itemprop="position" content="2">
</a>    </span>

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a href="/usgs/libcomcat/pulls" class="js-selected-navigation-item reponav-item" data-hotkey="g p" data-selected-links="repo_pulls /usgs/libcomcat/pulls" itemprop="url">
      <svg aria-hidden="true" class="octicon octicon-git-pull-request" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
      <span itemprop="name">Pull requests</span>
      <span class="counter">1</span>
      <meta itemprop="position" content="3">
</a>  </span>

    <a href="/usgs/libcomcat/projects" class="js-selected-navigation-item reponav-item" data-selected-links="repo_projects new_repo_project repo_project /usgs/libcomcat/projects">
      <svg aria-hidden="true" class="octicon octicon-project" height="16" version="1.1" viewBox="0 0 15 16" width="15"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
      Projects
      <span class="counter">0</span>
</a>


  <a href="/usgs/libcomcat/pulse" class="js-selected-navigation-item reponav-item" data-selected-links="pulse /usgs/libcomcat/pulse">
    <svg aria-hidden="true" class="octicon octicon-pulse" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M11.5 8L8.8 5.4 6.6 8.5 5.5 1.6 2.38 8H0v2h3.6l.9-1.8.9 5.4L9 8.5l1.6 1.5H14V8z"/></svg>
    Pulse
</a>
  <a href="/usgs/libcomcat/graphs" class="js-selected-navigation-item reponav-item" data-selected-links="repo_graphs repo_contributors /usgs/libcomcat/graphs">
    <svg aria-hidden="true" class="octicon octicon-graph" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M16 14v1H0V0h1v14h15zM5 13H3V8h2v5zm4 0H7V3h2v10zm4 0h-2V6h2v7z"/></svg>
    Graphs
</a>

</nav>

    </div>
  </div>

<div class="container new-discussion-timeline experiment-repo-nav">
  <div class="repository-content">

    
          

<a href="/usgs/libcomcat/blob/18266abc84a758d687bfb2c73757a605092667d4/README.md" class="d-none js-permalink-shortcut" data-hotkey="y">Permalink</a>

<!-- blob contrib key: blob_contributors:v21:6cf3d34c7b29bb7ac2865fa96313dad7 -->

<div class="file-navigation js-zeroclipboard-container">
  
<div class="select-menu branch-select-menu js-menu-container js-select-menu float-left">
  <button class=" btn btn-sm select-menu-button js-menu-target css-truncate" data-hotkey="w"
    
    type="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
      <i>Branch:</i>
      <span class="js-select-button css-truncate-target">master</span>
  </button>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax>

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <svg aria-label="Close" class="octicon octicon-x js-menu-close" height="16" role="img" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
        <span class="select-menu-title">Switch branches/tags</span>
      </div>

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="form-control js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" data-filter-placeholder="Filter branches/tags" class="js-select-menu-tab" role="tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" data-filter-placeholder="Find a tag…" class="js-select-menu-tab" role="tab">Tags</a>
            </li>
          </ul>
        </div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches" role="menu">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/usgs/libcomcat/blob/gh-pages/README.md"
               data-name="gh-pages"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                gh-pages
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open selected"
               href="/usgs/libcomcat/blob/master/README.md"
               data-name="master"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                master
              </span>
            </a>
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div>

    </div>
  </div>
</div>

  <div class="BtnGroup float-right">
    <a href="/usgs/libcomcat/find/master"
          class="js-pjax-capture-input btn btn-sm BtnGroup-item"
          data-pjax
          data-hotkey="t">
      Find file
    </a>
    <button aria-label="Copy file path to clipboard" class="js-zeroclipboard btn btn-sm BtnGroup-item tooltipped tooltipped-s" data-copied-hint="Copied!" type="button">Copy path</button>
  </div>
  <div class="breadcrumb js-zeroclipboard-target">
    <span class="repo-root js-repo-root"><span class="js-path-segment"><a href="/usgs/libcomcat"><span>libcomcat</span></a></span></span><span class="separator">/</span><strong class="final-path">README.md</strong>
  </div>
</div>



  <div class="commit-tease">
      <span class="float-right">
        <a class="commit-tease-sha" href="/usgs/libcomcat/commit/7b5ae7562a162d9db34c1594606b84a8c0fa6835" data-pjax>
          7b5ae75
        </a>
        <relative-time datetime="2017-02-01T18:40:04Z">Feb 1, 2017</relative-time>
      </span>
      <div>
        <img alt="@mhearne-usgs" class="avatar" height="20" src="https://avatars1.githubusercontent.com/u/303058?v=3&amp;s=40" width="20" />
        <a href="/mhearne-usgs" class="user-mention" rel="contributor">mhearne-usgs</a>
          <a href="/usgs/libcomcat/commit/7b5ae7562a162d9db34c1594606b84a8c0fa6835" class="message" data-pjax="true" title="Fixed readme.">Fixed readme.</a>
      </div>

    <div class="commit-tease-contributors">
      <button type="button" class="btn-link muted-link contributors-toggle" data-facebox="#blob_contributors_box">
        <strong>1</strong>
         contributor
      </button>
      
    </div>

    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header" data-facebox-id="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list" data-facebox-id="facebox-description">
          <li class="facebox-user-list-item">
            <img alt="@mhearne-usgs" height="24" src="https://avatars3.githubusercontent.com/u/303058?v=3&amp;s=48" width="24" />
            <a href="/mhearne-usgs">mhearne-usgs</a>
          </li>
      </ul>
    </div>
  </div>

<div class="file">
  <div class="file-header">
  <div class="file-actions">

    <div class="BtnGroup">
      <a href="/usgs/libcomcat/raw/master/README.md" class="btn btn-sm BtnGroup-item" id="raw-url">Raw</a>
        <a href="/usgs/libcomcat/blame/master/README.md" class="btn btn-sm js-update-url-with-hash BtnGroup-item" data-hotkey="b">Blame</a>
      <a href="/usgs/libcomcat/commits/master/README.md" class="btn btn-sm BtnGroup-item" rel="nofollow">History</a>
    </div>


        <button type="button" class="btn-octicon disabled tooltipped tooltipped-nw"
          aria-label="You must be signed in to make or propose changes">
          <svg aria-hidden="true" class="octicon octicon-pencil" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M0 12v3h3l8-8-3-3-8 8zm3 2H1v-2h1v1h1v1zm10.3-9.3L12 6 9 3l1.3-1.3a.996.996 0 0 1 1.41 0l1.59 1.59c.39.39.39 1.02 0 1.41z"/></svg>
        </button>
        <button type="button" class="btn-octicon btn-octicon-danger disabled tooltipped tooltipped-nw"
          aria-label="You must be signed in to make or propose changes">
          <svg aria-hidden="true" class="octicon octicon-trashcan" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M11 2H9c0-.55-.45-1-1-1H5c-.55 0-1 .45-1 1H2c-.55 0-1 .45-1 1v1c0 .55.45 1 1 1v9c0 .55.45 1 1 1h7c.55 0 1-.45 1-1V5c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm-1 12H3V5h1v8h1V5h1v8h1V5h1v8h1V5h1v9zm1-10H2V3h9v1z"/></svg>
        </button>
  </div>

  <div class="file-info">
      469 lines (350 sloc)
      <span class="file-info-divider"></span>
    20.7 KB
  </div>
</div>

  
  <div id="readme" class="readme blob instapaper_body">
    <article class="markdown-body entry-content" itemprop="text"><h2><a id="user-content-introduction" class="anchor" href="#introduction" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Introduction</h2>
<p>libcomcat is a project designed to provide command line equivalents to the ANSS ComCat search
<a href="http://comcat.cr.usgs.gov/fdsnws/event/1/">API</a>.  This code includes (so far):</p>
<ul>
<li>Three scripts:
<ul>
<li>getcomcat.py A script to download ComCat product contents (shakemap grids, origin quakeml, etc.)</li>
<li>getcsv.py A script to generate csv or tab separated text files with basic earthquake information.</li>
<li>getfixed.py A script to generate text files in one of two fixed-width formats: ISF and EHDF.</li>
</ul>
</li>
<li>Two code modules, libcomcat/comcat.py, and libcomcat/fixed.py, with functions supporting the above scripts.</li>
</ul>
<h2><a id="user-content-installation-and-dependencies" class="anchor" href="#installation-and-dependencies" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Installation and Dependencies</h2>
<hr>
<p>For users of anaconda or miniconda, do the following:</p>
<ul>
<li>git clone <a href="https://github.com/usgs/libcomcat.git">https://github.com/usgs/libcomcat.git</a></li>
<li>cd libcomcat</li>
<li>conda update conda</li>
<li>bash setup_env.sh</li>
<li>source activate comcat</li>
<li>cd ..</li>
<li>pip install --upgrade libcomcat/</li>
</ul>
<hr>
<p>Other users, see instructions below.</p>
<p>This package depends on numpy, the fundamental package for scientific computing with Python.
<a href="http://www.numpy.org/"></a><a href="http://www.numpy.org/">http://www.numpy.org/</a></p>
<p>and neicmap and neicio, part of an effort at the NEIC to create generally useful Python libraries from
the <a href="http://earthquake.usgs.gov/earthquakes/pager/">PAGER</a> source code.</p>
<p>The best way to install numpy is to use one of the Python distributions described here:</p>
<p><a href="http://www.scipy.org/install.html"></a><a href="http://www.scipy.org/install.html">http://www.scipy.org/install.html</a></p>
<p>Anaconda and Enthought distributions have been successfully tested with libcomcat.</p>
<p>Most of those distributions should include <em>pip</em>, a command line tool for installing and
managing Python packages.  You will use pip to install the other dependencies and libcomcat itself.</p>
<p>You will also need to install <em>git</em>, a source code management tool, for your platform.</p>
<p><a href="http://git-scm.com/downloads">http://git-scm.com/downloads</a></p>
<p>You may need to open a new terminal window to ensure that the newly installed versions of python, pip and git
are in your path.</p>
<p>To install neicmap and neicio:</p>
<p>pip install git+git://github.com/usgs/neicmap.git</p>
<p>pip install git+git://github.com/usgs/neicio.git</p>
<p>To install this package:</p>
<p>pip install git+git://github.com/usgs/libcomcat.git</p>
<p>The last command will install getcomcat.py, getcsv.py, and getfixed.py in your path.</p>
<h2><a id="user-content-uninstalling-and-updating" class="anchor" href="#uninstalling-and-updating" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Uninstalling and Updating</h2>
<p>To uninstall:</p>
<p>pip uninstall libcomcat</p>
<p>To update:</p>
<p>pip install -U git+git://github.com/usgs/libcomcat.git</p>
<h2><a id="user-content-application-programming-interface-api-usage" class="anchor" href="#application-programming-interface-api-usage" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Application Programming Interface (API) Usage</h2>
<p>The library code will be installed in
&lt;PATH_TO_PYTHON&gt;/lib/pythonX.Y/site-packages/libcomcat/.  Developers
should be able to use the functions in comcat.py and fixed.py by
importing them:</p>
<blockquote>
<blockquote>
<p>from libcomcat import comcat</p>
</blockquote>
</blockquote>
<blockquote>
<blockquote>
<p>from libcomcat import fixed</p>
</blockquote>
</blockquote>
<p>You can browse the API documentation for these two modules here:</p>
<p><a href="http://usgs.github.io/libcomcat/"></a><a href="http://usgs.github.io/libcomcat/">http://usgs.github.io/libcomcat/</a>.</p>
<h2><a id="user-content-usage-for-getcomcatpy" class="anchor" href="#usage-for-getcomcatpy" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Usage for getcomcat.py</h2>
<pre>usage: getcomcat.py [-h] [-o OUTPUTFOLDER] [-b lonmin lonmax latmin latmax]
                    [-s STARTTIME] [-e ENDTIME] [-a AFTER] [-m minmag maxmag]
                    [-c CATALOG] [-n CONTRIBUTOR] [-i EVENTID]
                    [-p PRODUCTPROPERTIES] [-t EVENTPROPERTIES] [-l] [-g]
                    PRODUCT [CONTENTLIST [CONTENTLIST ...]]

Download product content files from USGS ComCat.

    To download ShakeMap grid.xml files for a box around New Zealand during 2013:

    getcomcat.py shakemap grid.xml -o /home/user/newzealand -b 163.213 -178.945 -48.980 -32.324 -s 2013-01-01 -e 2014-01-01

    Note that when specifying a search box that crosses the -180/180 meridian, you simply specify longitudes
    as you would if you were not crossing that meridian.

    Note: Some product content files do not always have the same name, usually because they incorporate the event ID
    into the file name, such as with most of the files associated with the finite-fault product.  To download these files,
    you will need to input a unique fragment of the file name that can be matched in a search.

    For example, to retrieve all of the coulomb input files for the finite-fault product, you would construct your
    search like this:
    getcomcat.py finite-fault _coulomb.inp -o ~/tmp/chile -b -76.509 -49.804  -67.72 -17.427 -s 2007-01-01 -e 2016-05-01 -m 6.5 9.9

    To retrieve the moment rate function files, do this:
    getcomcat.py finite-fault .mr -o ~/tmp/chile -b -76.509 -49.804  -67.72 -17.427 -s 2007-01-01 -e 2016-05-01 -m 6.5 9.9


positional arguments:
  PRODUCT               The name of the desired product (shakemap, dyfi, etc.)
  CONTENTLIST           The names of the product contents (grid.xml,
                        stationlist.txt, etc.)

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUTFOLDER, --output-folder OUTPUTFOLDER
                        Folder where output files should be written.
  -b lonmin lonmax latmin latmax, --bounds lonmin lonmax latmin latmax
                        Bounds to constrain event search [lonmin lonmax latmin
                        latmax]
  -s STARTTIME, --start-time STARTTIME
                        Start time for search (defaults to ~30 days ago).
                        YYYY-mm-dd or YYYY-mm-ddTHH:MM:SS
  -e ENDTIME, --end-time ENDTIME
                        End time for search (defaults to current date/time).
                        YYYY-mm-dd or YYYY-mm-ddTHH:MM:SS
  -a AFTER, --after AFTER
                        Limit to events after specified time. YYYY-mm-dd or
                        YYYY-mm-ddTHH:MM:SS
  -m minmag maxmag, --mag-range minmag maxmag
                        Min/max magnitude to restrict search.
  -c CATALOG, --catalog CATALOG
                        Source catalog from which products derive (atlas,
                        centennial, etc.)
  -n CONTRIBUTOR, --contributor CONTRIBUTOR
                        Source contributor (who loaded product) (us, nc, etc.)
  -i EVENTID, --event-id EVENTID
                        Event ID from which to download product contents.
  -p PRODUCTPROPERTIES, --product-property PRODUCTPROPERTIES
                        Product property (reviewstatus:approved).
  -t EVENTPROPERTIES, --event-property EVENTPROPERTIES
                        Event property (alert:yellow, status:REVIEWED, etc.).
  -l, --list-url        Only list urls for contents in events that match
                        criteria.
  -g, --get-all-versions
                        Get products for every version of every event.
</pre>
<h2><a id="user-content-usage-for-getcsvpy" class="anchor" href="#usage-for-getcsvpy" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Usage for getcsv.py</h2>
<pre>usage: getcsv.py [-h] [-b lonmin lonmax latmin latmax] [-r lat lon rmax]
                 [-s STARTTIME] [-e ENDTIME] [-m minmag maxmag] [-c CATALOG]
                 [-n CONTRIBUTOR] [-o]
                 [-l {usmww,usmwb,usmwc,usmwr,gcmtmwc,cimwr,ncmwr}] [-a] [-g]
                 [-f {csv,tab}] [-x] [-v] [-d]

Download basic earthquake information in line format (csv, tab, etc.).

    To download basic event information (time,lat,lon,depth,magnitude) and moment tensor components for a box around New Zealand
    during 2013:

    getcsv.py -o -b 163.213 -178.945 -48.980 -32.324 -s 2013-01-01 -e 2014-01-01 &gt; nz.csv

    To limit that search to only those events with a US Mww moment tensor solution:

    getcsv.py -o -b 163.213 -178.945 -48.980 -32.324 -s 2013-01-01 -e 2014-01-01 -l usmww &gt; nz.csv

    To include all magnitudes (including source and type) for that same search, add the -g flag:

    getcsv.py -o -b 163.213 -178.945 -48.980 -32.324 -s 2013-01-01 -e 2014-01-01 -l usmww -g &gt; nz.csv

    To print the number of events that would be returned from the above query, and the maximum number of events supported
    by ONE ComCat query*:

    getcsv.py -x -o -b 163.213 -178.945 -48.980 -32.324 -s 2013-01-01 -e 2014-01-01

    To download events with fractional days, use the ISO 8601 combined date time format (YYYY-mm-ddTHH:MM:SS, YYYY-mm-ddTHH:MM:SS.s):
    getcsv.py -s 2015-01-01T00:00:00 -e 2015-01-01T01:15:00

    NOTE: Any start or end time where only date is specified (YYYY-mm-dd) will be translated to the beginning of that day.
    Thus, a start time of "2015-01-01" becomes "2015-01-01T:00:00:00" and an end time of "2015-01-02"
    becomes ""2015-01-02T:00:00:00".

    Events which do not have a value for a given field (moment tensor components, for example), will have the string "nan" instead.

    Note that when specifying a search box that crosses the -180/180 meridian, you simply specify longitudes
    as you would if you were not crossing that meridian (i.e., lonmin=179, lonmax=-179).  The program will resolve the
    discrepancy.


    *Queries that exceed this ComCat limit ARE supported by this software, by breaking up one large request into a number of
    smaller ones.  However, large queries, when also configured to retrieve moment tensor parameters, nodal plane angles, or
    moment tensor type can take a very long time to download.  The author has tested queries just over 20,000 events, and it
    can take ~90 minutes to complete.  This delay is caused by the fact that when this program has to retrieve moment tensor
    parameters, nodal plane angles, or moment tensor type, it must open a URL for EACH event and parse the data it finds.
    If these parameters are not requested, then the same request will return in much less time (~10 minutes or less for a
    20,000 event query).


optional arguments:
  -h, --help            show this help message and exit
  -b lonmin lonmax latmin latmax, --bounds lonmin lonmax latmin latmax
                        Bounds to constrain event search [lonmin lonmax latmin
                        latmax]
  -r lat lon rmax, --radius lat lon rmax
                        Search radius in KM (use instead of bounding box)
  -s STARTTIME, --start-time STARTTIME
                        Start time for search (defaults to ~30 days ago).
                        YYYY-mm-dd, YYYY-mm-ddTHH:MM:SS, or YYYY-mm-
                        ddTHH:MM:SS.s
  -e ENDTIME, --end-time ENDTIME
                        End time for search (defaults to current date/time).
                        YYYY-mm-dd, YYYY-mm-ddTHH:MM:SS, or YYYY-mm-
                        ddTHH:MM:SS.s
  -m minmag maxmag, --mag-range minmag maxmag
                        Min/max (authoritative) magnitude to restrict search.
  -c CATALOG, --catalog CATALOG
                        Source catalog from which products derive (atlas,
                        centennial, etc.)
  -n CONTRIBUTOR, --contributor CONTRIBUTOR
                        Source contributor (who loaded product) (us, nc, etc.)
  -o, --get-moment-components
                        Also extract moment-tensor components (including type
                        and derived hypocenter) where available.
  -l {usmww,usmwb,usmwc,usmwr,gcmtmwc,cimwr,ncmwr}, --limit-type {usmww,usmwb,usmwc,usmwr,gcmtmwc,cimwr,ncmwr}
                        Only extract moment-tensor components from given type.
  -a, --get-focal-angles
                        Also extract focal-mechanism angles (strike,dip,rake)
                        where available.
  -g, --get-all-magnitudes
                        Extract all magnitudes (with sources),authoritative
                        listed first.
  -f {csv,tab}, --format {csv,tab}
                        Output format
  -x, --count           Just return the number of events in search and maximum
                        allowed.
  -v, --verbose         Print progress
  -d, --debug           Check the USGS development server (only valid inside
                        USGS network).
</pre>
<h2><a id="user-content-usage-for-getfixedpy" class="anchor" href="#usage-for-getfixedpy" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Usage for getfixed.py</h2>
<pre>usage: getfixed.py [-h] [-b lonmin lonmax latmin latmax]
                   [-r lat lon rmin rmax] [-s STARTTIME] [-e ENDTIME]
                   [-m minmag maxmag] [-c CATALOG] [-n CONTRIBUTOR]
                   [-i EVENTID]
                   {isf,ehdf}

Download earthquake information in a fixed-width (ISF or EHDF) format.

    Retrieving many events:

    getfixed.py isf -b -105.010 -104.090 37.049 37.475 -s 2014-01-01 -e 2014-01-24 &gt; southern_colorado.isf

      
    This should print (to stderr) the ids of the events found in the search box, and then print (to stdout)
    the results in ISF format.

    Doing a radius search for multiple events:
    
    getfixed.py isf -r 35.786 -97.475 10 30 -s 2014-01-01 -e 2014-02-18 &gt; oklahoma.isf

    Retrieving a single event:

    getfixed.py isf -i usb000m4lb &gt; usb000m4lb.isf

    To retrieve events using a search box that spans the -180/180 meridian, simply specify longitudes
    as you would if you were not crossing that meridian:

    ./getfixed.py isf -b 177.605 -175.83 49.86 53.593 -s 2014-01-01 -e 2014-01-24 &gt; aleutians.isf

    You can repeat these procedures for the EHDF format.

    The ISF format is described here:
    http://www.isc.ac.uk/standards/isf/

    The EHDF format is described here:
    ftp://hazards.cr.usgs.gov/weekly/ehdf.txt
    

positional arguments:
  {isf,ehdf}            Output data in ISF format

optional arguments:
  -h, --help            show this help message and exit
  -b lonmin lonmax latmin latmax, --bounds lonmin lonmax latmin latmax
                        Bounds to constrain event search [lonmin lonmax latmin
                        latmax]
  -r lat lon rmin rmax, --radius lat lon rmin rmax
                        Min/max search radius in KM (use instead of bounding
                        box)
  -s STARTTIME, --start-time STARTTIME
                        Start time for search (defaults to ~30 days ago).
                        YYYY-mm-dd or YYYY-mm-ddTHH:MM:SS
  -e ENDTIME, --end-time ENDTIME
                        End time for search (defaults to current date/time).
                        YYYY-mm-dd or YYYY-mm-ddTHH:MM:SS
  -m minmag maxmag, --mag-range minmag maxmag
                        Min/max magnitude to restrict search.
  -c CATALOG, --catalog CATALOG
                        Source catalog from which products derive (atlas,
                        centennial, etc.)
  -n CONTRIBUTOR, --contributor CONTRIBUTOR
                        Source contributor (who loaded product) (us, nc, etc.)
  -i EVENTID, --id EVENTID
                        Output data in EHDF format
</pre>
<p>Usage for findid.py:</p>
<pre>usage: findid.py [-h] [-p time lat lon] [-r RADIUS] [-w WINDOW] [-f FILE] [-a]
                 [-u] [-v]

Find the id(s) of the closest earthquake to input parameters. 

    To print the authoritative id of the event closest in time and space inside a 100 km, 16 second window to "2015-03-29T23:48:31,-4.763,152.561":

    findid.py -p 2015-03-29T23:48:31 -4.763 152.561

    To repeat that query but with a custom distance/time window of 50km and 5 seconds:

    findid.py -r 50 -w 5 -p 2015-03-29T23:48:31 -4.763 152.561

    To print the authoritative id of the event closest in time and space to "2015-03-29T23:48:31,-4.763,152.561" AND
    the url of said event:

    findid.py -u -p 2015-03-29T23:48:31 -4.763 152.561

    To print all of the ids associated with the event closest to above:

    findid.py -a -p 2015-03-29T23:48:31 -4.763 152.561

    To print the id(s), time/distance deltas, and azimuth from input to nearest event:

    findid.py -v -p 2015-03-29T23:48:31 -4.763 152.561

    To find the ids for events found in a CSV file (time,lat,lon,...):
    (Create a file by doing the following: getcsv.py -s 2015-04-07 -e 2015-04-08T15:00:00 -m 4.0 5.5 | cut -f2,3,4,5,6,7 -d',' &gt; eventlist.csv)
    ./findid.py -f eventlist.csv
    Output will be the input CSV data, with id added as the first column.

    If -u option is supplied, the url will be the second column.

    Notes:
     - The time format at the command line must be of the form "YYYY-MM-DDTHH:MM:SS".  The time format in an input csv file
     can be either :YYYY-MM-DDTHH:MM:SS" OR "YYYY-MM-DD HH:MM:SS".  This is because on the command line the argument parser 
     would be confused by the space between the date and the time, whereas in the csv file the input files are being split
     by commas.
     - Supplying the -a option with the -f option has no effect.
    

optional arguments:
  -h, --help            show this help message and exit
  -p time lat lon, --params time lat lon
                        Input time, lat and lon to use for search.
  -r RADIUS, --radius RADIUS
                        Change search radius from default of 100 km.
  -w WINDOW, --window WINDOW
                        Change time window of 16 seconds.
  -f FILE, --file FILE  Parse time,lat,lon from input csv file, which can have
                        a header row but must have time,lat,lon as first three
                        columns. Time format can be either YYYY-MM-DDTHH:MM:SS
                        OR YYYY-MM-DD HH:MM:SS. Output will have an "id"
                        column prepended, and a "url" column second (if -u
                        option selected), followed by the input columns of
                        data.
  -a, --all             Print all ids associated with event.
  -u, --url             Print URL associated with event.
  -v, --verbose         Print time/distance deltas, and azimuth from input
                        parameters to event.
</pre>
<p>Usage for getellipse.py:</p>
<pre>usage: getellipse.py [-h] [-t alen blen clen azimuth plunge rotation]
                     [-r AAzim APlunge ALen BAzim BPlunge BLen CAzim CPlunge CLen]
                     [-q alen blen clen azimuth plunge rotation ndef stderr isfixed]
                     [-m AAzim APlunge ALen BAzim BPlunge BLen CAzim CPlunge CLen ndef stderr isfixed]

Convert between various representation of earthquake error ellipse.

    Tait-Bryan (QuakeML) representation to 3x3 matrix representation:

    getellipse.py -t 16.0 6.1 10.9 139.0 6.0 88.9075

    --------------------------------------------------------------
    SemiMajorAxis       : Azimuth 139.0 Plunge   6.0 Length  16.0
    SemiMinorAxis       : Azimuth 308.7 Plunge  83.9 Length   6.1
    SemiIntermediateAxis: Azimuth  48.9 Plunge   1.1 Length  10.9 
    -------------------------------------------------------------- 

    Tait-Bryan (QuakeML) representation to surface projection:

    getellipse.py -q 16.0 6.1 10.9 139.0 6.0 88.9075 95 0.76 0

    -------------------------------------------------------
    Surface Ellipse: Major:  13.7 Minor   9.4 Azimuth 319.1  
    -------------------------------------------------------

    3x3 Matrix representation to surface projection:

    getellipse.py -m 139.0 6.0 16.0 308.7 83.9 6.1 48.9 1.1 10.9 95 0.76 0

    -------------------------------------------------------
    Surface Ellipse: Major:  13.7 Minor   9.4 Azimuth 319.1
    -------------------------------------------------------
    
    3x3 matrix representation to Tait-Bryan (QuakeML) representation:

    getellipse.py -r 139.0 6.0 16.0 308.7 83.9 6.1 48.9 1.1 10.9

    -----------------------------------------------------------------------------
    SemiMajor Axis       : Azimuth 139.0 Plunge   6.0 Rotation  88.9 Length  16.0
    SemiMinor Axis       : Azimuth   nan Plunge   nan Rotation   nan Length   6.1
    SemiIntermediate Axis: Azimuth   nan Plunge   nan Rotation   nan Length  10.9
    -----------------------------------------------------------------------------
    

optional arguments:
  -h, --help            show this help message and exit
  -t alen blen clen azimuth plunge rotation, --tait2matrix alen blen clen azimuth plunge rotation
                        Convert Tait-Bryan error ellipse to 3x3 matrix
  -r AAzim APlunge ALen BAzim BPlunge BLen CAzim CPlunge CLen, --matrix2tait AAzim APlunge ALen BAzim BPlunge BLen CAzim CPlunge CLen
                        Convert 3x3 matrix error ellipse to Tait-Bryan
                        representation
  -q alen blen clen azimuth plunge rotation ndef stderr isfixed, --tait2surface alen blen clen azimuth plunge rotation ndef stderr isfixed
                        Project Tait-Bryan error ellipse to surface
  -m AAzim APlunge ALen BAzim BPlunge BLen CAzim CPlunge CLen ndef stderr isfixed, --matrix2surface AAzim APlunge ALen BAzim BPlunge BLen CAzim CPlunge CLen ndef stderr isfixed
                        Project 3x3 matrix error ellipse to surface
</pre>
<p>Usage for getimpact.py:</p>
<pre>usage: getimpact.py [-h] eventID

Return the eventid,origin time,lat,lon,depth,magnitude,impact text for a given
input event ID. If no impact-text product is found, then the text returned
will be an empty string "". getimpact.py eventid Example: getimpact.py
us10003vki Returns: us10003vki,2015-11-07
17:37:49,8.5000,-71.5000,5.0,4.9,"Felt (V) at Ejido."

positional arguments:
  eventID     Event ID (i.e., us10003vki).

optional arguments:
  -h, --help  show this help message and exit
</pre>
<h2><a id="user-content-libcomcat-api-for-developers" class="anchor" href="#libcomcat-api-for-developers" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>libcomcat API for Developers</h2>
<p>The functions that are most likely of interest to developers are in
<a href="/usgs/libcomcat/blob/master/html/index.html">libcomcat/comcat</a></p>
</article>
  </div>

</div>

<button type="button" data-facebox="#jump-to-line" data-facebox-class="linejump" data-hotkey="l" class="d-none">Jump to Line</button>
<div id="jump-to-line" style="display:none">
  <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="" class="js-jump-to-line-form" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
    <input class="form-control linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" aria-label="Jump to line" autofocus>
    <button type="submit" class="btn">Go</button>
</form></div>


  </div>
  <div class="modal-backdrop js-touch-events"></div>
</div>

    </div>
  </div>

  </div>

      <div class="container site-footer-container">
  <div class="site-footer" role="contentinfo">
    <ul class="site-footer-links float-right">
        <li><a href="https://github.com/contact" data-ga-click="Footer, go to contact, text:contact">Contact GitHub</a></li>
      <li><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
      <li><a href="https://shop.github.com" data-ga-click="Footer, go to shop, text:shop">Shop</a></li>
        <li><a href="https://github.com/blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a href="https://github.com/about" data-ga-click="Footer, go to about, text:about">About</a></li>

    </ul>

    <a href="https://github.com" aria-label="Homepage" class="site-footer-mark" title="GitHub">
      <svg aria-hidden="true" class="octicon octicon-mark-github" height="24" version="1.1" viewBox="0 0 16 16" width="24"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
</a>
    <ul class="site-footer-links">
      <li>&copy; 2017 <span title="0.06637s from github-fe152-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="https://github.com/site/terms" data-ga-click="Footer, go to terms, text:terms">Terms</a></li>
        <li><a href="https://github.com/site/privacy" data-ga-click="Footer, go to privacy, text:privacy">Privacy</a></li>
        <li><a href="https://github.com/security" data-ga-click="Footer, go to security, text:security">Security</a></li>
        <li><a href="https://status.github.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
        <li><a href="https://help.github.com" data-ga-click="Footer, go to help, text:help">Help</a></li>
    </ul>
  </div>
</div>



  

  <div id="ajax-error-message" class="ajax-error-message flash flash-error">
    <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.865 1.52c-.18-.31-.51-.5-.87-.5s-.69.19-.87.5L.275 13.5c-.18.31-.18.69 0 1 .19.31.52.5.87.5h13.7c.36 0 .69-.19.86-.5.17-.31.18-.69.01-1L8.865 1.52zM8.995 13h-2v-2h2v2zm0-3h-2V6h2v4z"/></svg>
    <button type="button" class="flash-close js-flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
    </button>
    You can't perform that action at this time.
  </div>


    <script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/compat-8a4318ffea09a0cdb8214b76cf2926b9f6a0ced318a317bed419db19214c690d.js"></script>
    <script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/frameworks-6d109e75ad8471ba415082726c00c35fb929ceab975082492835f11eca8c07d9.js"></script>
    <script async="async" crossorigin="anonymous" src="https://assets-cdn.github.com/assets/github-225a22ae2420e34ab23c6a4131040d17c0ceaf223392ec557641a8412e391a23.js"></script>
    
    
    
    
  <div class="js-stale-session-flash stale-session-flash flash flash-warn flash-banner d-none">
    <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.865 1.52c-.18-.31-.51-.5-.87-.5s-.69.19-.87.5L.275 13.5c-.18.31-.18.69 0 1 .19.31.52.5.87.5h13.7c.36 0 .69-.19.86-.5.17-.31.18-.69.01-1L8.865 1.52zM8.995 13h-2v-2h2v2zm0-3h-2V6h2v4z"/></svg>
    <span class="signed-in-tab-flash">You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
    <span class="signed-out-tab-flash">You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
  </div>
  <div class="facebox" id="facebox" style="display:none;">
  <div class="facebox-popup">
    <div class="facebox-content" role="dialog" aria-labelledby="facebox-header" aria-describedby="facebox-description">
    </div>
    <button type="button" class="facebox-close js-facebox-close" aria-label="Close modal">
      <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
    </button>
  </div>
</div>


  </body>
</html>

