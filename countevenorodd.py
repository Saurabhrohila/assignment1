<!DOCTYPE html>
<!-- saved from url=(0026)http://localhost:8888/tree -->
<html lang="en-gb"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    

    <title>Home Page - Select or create a notebook</title>
    <link id="favicon" rel="shortcut icon" type="image/x-icon" href="http://localhost:8888/static/base/images/favicon.ico?v=50afa725b5de8b00030139d09b38620224d4e7dba47c07ef0e86d4643f30c9bfe6bb7e1a4a1c561aa32834480909a4b6fe7cd1e17f7159330b6b5914bf45a880">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <link rel="stylesheet" href="./countevenorodd_files/jquery-ui.min.css" type="text/css">
    <link rel="stylesheet" href="./countevenorodd_files/jquery.typeahead.min.css" type="text/css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    
    <link rel="stylesheet" href="./countevenorodd_files/style.min.css" type="text/css">
    
    <link rel="stylesheet" href="./countevenorodd_files/custom.css" type="text/css">
    <script src="./countevenorodd_files/promise.min.js.download" type="text/javascript" charset="utf-8"></script>
    <script src="./countevenorodd_files/react.production.min.js.download" type="text/javascript"></script>
    <script src="./countevenorodd_files/react-dom.production.min.js.download" type="text/javascript"></script>
    <script src="./countevenorodd_files/index.js.download" type="text/javascript"></script>
    <script src="./countevenorodd_files/require.js.download" type="text/javascript" charset="utf-8"></script>
    <script>
      require.config({
          
          urlArgs: "v=20211003124239",
          
          baseUrl: '/static/',
          paths: {
            'auth/js/main': 'auth/js/main.min',
            custom : '/custom',
            nbextensions : '/nbextensions',
            kernelspecs : '/kernelspecs',
            underscore : 'components/underscore/underscore-min',
            backbone : 'components/backbone/backbone-min',
            jed: 'components/jed/jed',
            jquery: 'components/jquery/jquery.min',
            json: 'components/requirejs-plugins/src/json',
            text: 'components/requirejs-text/text',
            bootstrap: 'components/bootstrap/dist/js/bootstrap.min',
            bootstraptour: 'components/bootstrap-tour/build/js/bootstrap-tour.min',
            'jquery-ui': 'components/jquery-ui/jquery-ui.min',
            moment: 'components/moment/min/moment-with-locales',
            codemirror: 'components/codemirror',
            termjs: 'components/xterm.js/xterm',
            typeahead: 'components/jquery-typeahead/dist/jquery.typeahead.min',
          },
          map: { // for backward compatibility
              "*": {
                  "jqueryui": "jquery-ui",
              }
          },
          shim: {
            typeahead: {
              deps: ["jquery"],
              exports: "typeahead"
            },
            underscore: {
              exports: '_'
            },
            backbone: {
              deps: ["underscore", "jquery"],
              exports: "Backbone"
            },
            bootstrap: {
              deps: ["jquery"],
              exports: "bootstrap"
            },
            bootstraptour: {
              deps: ["bootstrap"],
              exports: "Tour"
            },
            "jquery-ui": {
              deps: ["jquery"],
              exports: "$"
            }
          },
          waitSeconds: 30,
      });

      require.config({
          map: {
              '*':{
                'contents': 'services/contents',
              }
          }
      });

      // error-catching custom.js shim.
      define("custom", function (require, exports, module) {
          try {
              var custom = require('custom/custom');
              console.debug('loaded custom.js');
              return custom;
          } catch (e) {
              console.error("error loading custom.js", e);
              return {};
          }
      })

    document.nbjs_translations = {"domain": "nbjs", "locale_data": {"nbjs": {"": {"domain": "nbjs"}}}};
    document.documentElement.lang = navigator.language.toLowerCase();
    </script>

    
    

<script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="services/contents" src="./countevenorodd_files/contents.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="custom/custom" src="./countevenorodd_files/custom.js.download"></script></head>

<body class="" data-jupyter-api-token="fec61819c0b1c2c5e83711d13b7cca54ca648714a3138eb0" data-base-url="/" data-notebook-path="" data-terminals-available="True" data-server-root="C:\Users\dell" dir="ltr" data-new-gr-c-s-check-loaded="14.1031.0" data-gr-ext-installed="">

<noscript>
    <div id='noscript'>
      Jupyter Notebook requires JavaScript.<br>
      Please enable it to proceed. 
  </div>
</noscript>

<div id="header" role="navigation" aria-label="Top Menu" style="display: block;">
  <div id="header-container" class="container">
  <div id="ipython_notebook" class="nav navbar-brand"><a href="http://localhost:8888/tree?token=fec61819c0b1c2c5e83711d13b7cca54ca648714a3138eb0" title="dashboard">
      <img src="./countevenorodd_files/logo.png" alt="Jupyter Notebook">
  </a></div>

  
  <span class="flex-spacer"></span>
  
  
  
    <span id="shutdown_widget">
      <button id="shutdown" class="btn btn-sm navbar-btn" title="Stop the Jupyter server">
          Quit
      </button>
    </span>
  

  
  
  
  

    <span id="login_widget">
      
        <button id="logout" class="btn btn-sm navbar-btn">Logout</button>
      
    </span>

  

  
  
  </div>
  <div class="header-bar"></div>

  
  
</div>

<div id="site" style="display: block; height: 527px;">


  <div id="ipython-main-app" class="container">
    <div id="tab_content" class="tabbable" role="main">
      <ul id="tabs" class="nav nav-tabs">
        <li class="active"><a href="http://localhost:8888/tree#notebooks" data-toggle="tab">Files</a></li>
        <li><a href="http://localhost:8888/tree#running" data-toggle="tab">Running</a></li>
        <li><a href="http://localhost:8888/tree#clusters" data-toggle="tab" class="clusters_tab_link">Clusters</a></li>
      </ul>
      <div class="tab-content">
        <div id="notebooks" class="tab-pane active">
          <div id="notebook_toolbar" class="row list_toolbar">
            <div class="col-sm-8 no-padding">
              <div class="dynamic-instructions" style="display: none;">
                Select items to perform actions on them.
              </div>
              <div class="dynamic-buttons">
                  <button title="Duplicate selected" aria-label="Duplicate selected" class="duplicate-button btn btn-default btn-xs" aria-describedby="tooltip1" style="display: inline-block;">Duplicate </button>
                  <div role="tooltip" id="tooltip1">Duplicate selected</div>
                  <button title="Rename selected" aria-label="Rename selected" class="rename-button btn btn-default btn-xs" aria-describedby="tooltip2" style="display: inline-block;">Rename</button>
                  <div role="tooltip" id="tooltip2">Rename selected</div> 
                  <button title="Move selected" aria-label="Move selected" class="move-button btn btn-default btn-xs" aria-describedby="tooltip3" style="display: inline-block;">Move</button>
                  <div role="tooltip" id="tooltip3">Move selected</div> 
                  <button title="Download selected" aria-label="Download selected" class="download-button btn btn-default btn-xs" aria-describedby="tooltip4" style="display: inline-block;">Download</button>
                  <div role="tooltip" id="tooltip4">Download selected</div>
                  <button title="Shutdown selected notebook(s)" aria-label="Shutdown selected notebook(s)" class="shutdown-button btn btn-default btn-xs btn-warning" aria-describedby="tooltip5" style="display: none;">Shutdown</button>
                  <div role="tooltip" id="tooltip5">Shutdown selected notebook(s)</div>  
                  <button title="View selected" aria-label="View selected" class="view-button btn btn-default btn-xs" aria-describedby="tooltip6" style="display: inline-block;">View</button>
                  <div role="tooltip" id="tooltip6">View selected</div> 
                  <button title="Edit selected" aria-label="Edit selected" class="edit-button btn btn-default btn-xs" aria-describedby="tooltip7" style="display: inline-block;">Edit</button>
                  <div role="tooltip" id="tooltip7">Edit selected</div>  
                  <button title="Delete selected" aria-label="Delete selected" class="delete-button btn btn-default btn-xs btn-danger" aria-describedby="tooltip8" style="display: inline-block;">
                    <i class="fa fa-trash"></i>
                  </button>
                  <div role="tooltip" id="tooltip8">Delete selected</div>
              </div>
            </div>
            <div class="col-sm-4 no-padding tree-buttons">
              <div class="pull-right">
                <form id="alternate_upload" class="alternate_upload">
                  <span id="notebook_list_info" class="toolbar_info">
                  <span id="upload_span" class="btn btn-xs btn-default btn-upload" role="button" tabindex="0">
                    <input id="upload_span_input" title="Click to browse for a file to upload." type="file" name="datafile" class="fileinput" multiple="multiple" tabindex="-1">
                    Upload
                  </span>
                  </span>
                </form>
                <div id="new-buttons" class="btn-group">
                  <button class="dropdown-toggle btn btn-default btn-xs" id="new-dropdown-button" data-toggle="dropdown">
                  <span>New</span>
                  <span class="caret"></span>
                  <span class="sr-only">Toggle Dropdown</span>
                  </button>
                  <ul id="new-menu" class="dropdown-menu" role="menu">
                    <li role="menuitem" class="dropdown-header" id="notebook-kernels">Notebook:</li><li id="kernel-python3"><a aria-label="python3" role="menuitem" href="http://localhost:8888/tree#" title="Create a new notebook with Python 3">Python 3</a></li>
                    <li role="presentation" class="divider"></li>
                    <li role="menuitem" class="dropdown-header">Other:</li>
                    <li role="none" id="new-file">
                        <a role="menuitem" tabindex="-1" href="http://localhost:8888/tree#">Text File</a>
                    </li>
                    <li role="none" id="new-folder">
                        <a role="menuitem" tabindex="-1" href="http://localhost:8888/tree#">Folder</a>
                    </li>
                    
                    <li role="none" id="new-terminal">
                        <a role="menuitem" tabindex="-1" href="http://localhost:8888/tree#">Terminal</a>
                    </li>
                    
                  </ul>
                </div>
                <div class="btn-group">
                    <button id="refresh_notebook_list" title="Refresh notebook list" aria-label="Refresh notebook list" class="btn btn-default btn-xs"><i class="fa fa-refresh"></i></button>
                </div>
              </div>
            </div>
          </div>
          <div id="notebook_list" class="list_container">
            <div id="notebook_list_header" class="row list_header">
              <div class="btn-group dropdown" id="tree-selector">
                <button title="Select All / None" aria-label="Selected, 1 items" type="button" class="btn btn-default btn-xs" id="button-select-all" role="checkbox">
                  <input type="checkbox" class="pull-left tree-selector" id="select-all" tabindex="-1"><span id="counter-select-all">1</span>
                </button>
                <button title="Select Folders/All Notebooks/Running/Files" class="btn btn-default btn-xs dropdown-toggle" type="button" id="tree-selector-btn" data-toggle="dropdown" aria-expanded="true">
                  <span class="sr-only">checkbox</span>
                  <span class="caret"></span>
                  <span class="sr-only">Toggle Dropdown</span>
                </button>
                <ul id="selector-menu" class="dropdown-menu" role="menu" aria-labelledby="tree-selector-btn">
                  <li role="none"><a id="select-folders" role="menuitem" tabindex="-1" href="http://localhost:8888/tree#" title="Select All Folders"><i class="menu_icon folder_icon icon-fixed-width"></i>&nbsp;Folders</a></li>
                  <li role="none"><a id="select-notebooks" role="menuitem" tabindex="-1" href="http://localhost:8888/tree#" title="Select All Notebooks"><i class="menu_icon notebook_icon icon-fixed-width"></i>&nbsp;All Notebooks</a></li>
                  <li role="none"><a id="select-running-notebooks" role="menuitem" tabindex="-1" href="http://localhost:8888/tree#" title="Select Running Notebooks"><i class="menu_icon running_notebook_icon icon-fixed-width"></i>&nbsp;Running</a></li>
                  <li role="none"><a id="select-files" role="menuitem" tabindex="-1" href="http://localhost:8888/tree#" title="Select All Files"><i class="menu_icon file_icon icon-fixed-width"></i>&nbsp;Files</a></li>
                </ul>
              </div>
              <div id="project_name">
                <ul class="breadcrumb"><li><a href="http://localhost:8888/tree" title="Link to root folder"><i class="fa fa-folder"></i></a></li><li><a href="http://localhost:8888/tree"></a></li></ul>
              </div>
              <div id="sort_buttons" class="pull-right">
                <div id="sort_name" class="sort_button">
                  <button type="button" class="btn btn-xs btn-default sort-action" id="sort-name" aria-label="Sort by name">
                        Name
                        <i class="fa fa-arrow-down"></i>
                  </button>
                </div>
                <div id="last_modified" class="sort_button">
                    <button type="button" class="btn btn-xs btn-default sort-action" id="last-modified" aria-label="Sort by last modified">
                        Last Modified
                        <i class="fa"></i>
                    </button>
                </div>
                <div id="file_size" class="sort_button">
                    <button type="button" class="btn btn-xs btn-default sort-action" id="file-size" aria-label="Sort by file size">
                        File size
                        <i class="fa"></i>
                    </button>
                </div>
              </div>
            </div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/anaconda3"><span class="item_name">anaconda3</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2021-09-22 21:14">11 days ago</span><span class="file_size pull-right">&nbsp;</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Contacts"><span class="item_name">Contacts</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2021-09-24 13:52">9 days ago</span><span class="file_size pull-right">&nbsp;</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Desktop"><span class="item_name">Desktop</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2021-09-28 10:39">5 days ago</span><span class="file_size pull-right">&nbsp;</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Documents"><span class="item_name">Documents</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2021-10-03 13:04">seconds ago</span><span class="file_size pull-right">&nbsp;</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Downloads"><span class="item_name">Downloads</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2021-10-03 12:45">19 minutes ago</span><span class="file_size pull-right">&nbsp;</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Favorites"><span class="item_name">Favorites</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2021-09-24 13:52">9 days ago</span><span class="file_size pull-right">&nbsp;</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Links"><span class="item_name">Links</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2021-09-24 13:52">9 days ago</span><span class="file_size pull-right">&nbsp;</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Music"><span class="item_name">Music</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2021-09-24 13:52">9 days ago</span><span class="file_size pull-right">&nbsp;</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Pictures"><span class="item_name">Pictures</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2021-09-24 13:52">9 days ago</span><span class="file_size pull-right">&nbsp;</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Saved%20Games"><span class="item_name">Saved Games</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2021-09-24 13:52">9 days ago</span><span class="file_size pull-right">&nbsp;</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Searches"><span class="item_name">Searches</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2021-09-24 13:52">9 days ago</span><span class="file_size pull-right">&nbsp;</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Videos"><span class="item_name">Videos</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2021-09-24 13:52">9 days ago</span><span class="file_size pull-right">&nbsp;</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/Untitled.ipynb" target="_blank"><span class="item_name">Untitled.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2021-09-23 00:12">11 days ago</span><span class="file_size pull-right">72 B</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/Untitled1.ipynb" target="_blank"><span class="item_name">Untitled1.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2021-09-23 00:13">11 days ago</span><span class="file_size pull-right">72 B</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/Untitled10.ipynb" target="_blank"><span class="item_name">Untitled10.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2021-09-27 12:22">6 days ago</span><span class="file_size pull-right">2.53 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/Untitled11.ipynb" target="_blank"><span class="item_name">Untitled11.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2021-09-27 19:40">6 days ago</span><span class="file_size pull-right">576 B</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/Untitled12.ipynb" target="_blank"><span class="item_name">Untitled12.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2021-09-29 20:04">4 days ago</span><span class="file_size pull-right">896 B</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/Untitled13.ipynb" target="_blank"><span class="item_name">Untitled13.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2021-10-01 20:23">2 days ago</span><span class="file_size pull-right">2.72 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/Untitled14.ipynb" target="_blank"><span class="item_name">Untitled14.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2021-10-02 10:20">a day ago</span><span class="file_size pull-right">1.27 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/Untitled15.ipynb" target="_blank"><span class="item_name">Untitled15.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2021-10-02 10:37">a day ago</span><span class="file_size pull-right">1.15 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/Untitled16.ipynb" target="_blank"><span class="item_name">Untitled16.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2021-10-02 11:33">a day ago</span><span class="file_size pull-right">1.31 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/Untitled17.ipynb" target="_blank"><span class="item_name">Untitled17.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2021-10-02 11:57">a day ago</span><span class="file_size pull-right">1.36 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/Untitled18.ipynb" target="_blank"><span class="item_name">Untitled18.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2021-10-02 12:38">a day ago</span><span class="file_size pull-right">2.01 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/Untitled19.ipynb" target="_blank"><span class="item_name">Untitled19.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2021-10-02 23:54">13 hours ago</span><span class="file_size pull-right">2.26 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/Untitled2.ipynb" target="_blank"><span class="item_name">Untitled2.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2021-09-23 01:14">10 days ago</span><span class="file_size pull-right">72 B</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/Untitled20.ipynb" target="_blank"><span class="item_name">Untitled20.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2021-10-03 01:00">12 hours ago</span><span class="file_size pull-right">2.85 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/Untitled21.ipynb" target="_blank"><span class="item_name">Untitled21.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2021-10-03 11:17">2 hours ago</span><span class="file_size pull-right">1.91 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/Untitled3.ipynb" target="_blank"><span class="item_name">Untitled3.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2021-09-23 15:02">10 days ago</span><span class="file_size pull-right">1.59 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/Untitled4.ipynb" target="_blank"><span class="item_name">Untitled4.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2021-09-23 21:29">10 days ago</span><span class="file_size pull-right">2.21 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/Untitled5.ipynb" target="_blank"><span class="item_name">Untitled5.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2021-09-24 12:32">9 days ago</span><span class="file_size pull-right">3.67 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/Untitled6.ipynb" target="_blank"><span class="item_name">Untitled6.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2021-09-24 19:58">9 days ago</span><span class="file_size pull-right">1.7 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/Untitled7.ipynb" target="_blank"><span class="item_name">Untitled7.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2021-09-25 11:17">8 days ago</span><span class="file_size pull-right">2.7 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/Untitled8.ipynb" target="_blank"><span class="item_name">Untitled8.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2021-09-27 10:16">6 days ago</span><span class="file_size pull-right">2.91 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/Untitled9.ipynb" target="_blank"><span class="item_name">Untitled9.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2021-09-27 11:41">6 days ago</span><span class="file_size pull-right">3.11 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon file_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/edit/aman.py" target="_blank"><span class="item_name">aman.py</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2021-10-02 11:35">a day ago</span><span class="file_size pull-right">1.32 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon file_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/edit/count%20even%20and%20%20odd%20number.py" target="_blank"><span class="item_name">count even and  odd number.py</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2021-10-02 10:46">a day ago</span><span class="file_size pull-right">1.15 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon file_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/edit/fibonacci.py" target="_blank"><span class="item_name">fibonacci.py</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2021-10-02 11:59">a day ago</span><span class="file_size pull-right">1.4 kB</span></div></div></div></div>
          </div>
        </div>
        <div id="running" class="tab-pane">
          <div id="running_toolbar" class="row list_toolbar">
            <div class="col-sm-8 no-padding">
              <span id="running_list_info" class="toolbar_info">Currently running Jupyter processes</span>
            </div>
            <div class="col-sm-4 no-padding tree-buttons">
              <span id="running_buttons" class="pull-right toolbar_buttons">
              <button id="refresh_running_list" title="Refresh running list" aria-label="Refresh running list" class="btn btn-default btn-xs"><i class="fa fa-refresh"></i></button>
              </span>
            </div>
          </div>
          <div class="panel-group" id="accordion">
            <div class="panel panel-default">
              <div class="panel-heading">
                <a data-toggle="collapse" data-target="#collapseOne" href="http://localhost:8888/tree#">
                  Terminals
                <i class="fa fa-caret-down"></i></a>
              </div>
              <div id="collapseOne" class=" collapse in">
                <div class="panel-body">
                  <div id="terminal_list" class="list_container">
                    <div id="terminal_list_header" class="row list_placeholder">
                    
                      <div> There are no terminals running. </div>
                    
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="panel panel-default">
              <div class="panel-heading">
                <a data-toggle="collapse" data-target="#collapseTwo" href="http://localhost:8888/tree#">
                  Notebooks
                <i class="fa fa-caret-down"></i></a>
              </div>
              <div id="collapseTwo" class=" collapse in">
                <div class="panel-body">
                  <div id="running_list" class="list_container">
                    <div id="running_list_placeholder" class="row list_placeholder">
                      <div> There are no notebooks running. </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div id="clusters" class="tab-pane">
          Clusters tab is now provided by IPython parallel.
          See '<a href="https://github.com/ipython/ipyparallel">IPython parallel</a>' for installation details.
        </div>
      </div><!-- class:tab-content -->
    </div><!-- id:tab_content -->
  </div><!-- ipython-main-app  -->


</div>





    

    <script type="text/javascript">
      ('#element').tooltip('enable')
    </script>

<script src="./countevenorodd_files/main.min.js.download" type="text/javascript" charset="utf-8"></script>



<script type="text/javascript">
  function _remove_token_from_url() {
    if (window.location.search.length <= 1) {
      return;
    }
    var search_parameters = window.location.search.slice(1).split('&');
    for (var i = 0; i < search_parameters.length; i++) {
      if (search_parameters[i].split('=')[0] === 'token') {
        // remote token from search parameters
        search_parameters.splice(i, 1);
        var new_search = '';
        if (search_parameters.length) {
          new_search = '?' + search_parameters.join('&');
        }
        var new_url = window.location.origin + 
                      window.location.pathname + 
                      new_search + 
                      window.location.hash;
        window.history.replaceState({}, "", new_url);
        return;
      }
    }
  }
  _remove_token_from_url();
</script>


</body><grammarly-desktop-integration data-grammarly-shadow-root="true"></grammarly-desktop-integration></html>