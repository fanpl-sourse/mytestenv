webpackJsonpSm_name_([18],{1938:function(n,t,i){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var e,o=i(133),r=(i.n(o),i(0)),u=i.n(r),c=(i(2629),i(1)),a=i.n(c),l=i(6),s=i.n(l),f=i(3),d=i(2632),h=i(2633),b=i(2254),m=i(4),v=this&&this.__extends||(e=function(n,t){return(e=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(n,t){n.__proto__=t}||function(n,t){for(var i in t)t.hasOwnProperty(i)&&(n[i]=t[i])})(n,t)},function(n,t){function i(){this.constructor=n}e(n,t),n.prototype=null===t?Object.create(t):(i.prototype=t.prototype,new i)}),p=this&&this.__assign||function(){return(p=Object.assign||function(n){for(var t,i=1,e=arguments.length;i<e;i++)for(var o in t=arguments[i])Object.prototype.hasOwnProperty.call(t,o)&&(n[o]=t[o]);return n}).apply(this,arguments)},g=this&&this.__awaiter||function(n,t,i,e){return new(i||(i=Promise))(function(o,r){function u(n){try{a(e.next(n))}catch(n){r(n)}}function c(n){try{a(e.throw(n))}catch(n){r(n)}}function a(n){var t;n.done?o(n.value):(t=n.value,t instanceof i?t:new i(function(n){n(t)})).then(u,c)}a((e=e.apply(n,t||[])).next())})},w=this&&this.__generator||function(n,t){var i,e,o,r,u={label:0,sent:function(){if(1&o[0])throw o[1];return o[1]},trys:[],ops:[]};return r={next:c(0),throw:c(1),return:c(2)},"function"==typeof Symbol&&(r[Symbol.iterator]=function(){return this}),r;function c(r){return function(c){return function(r){if(i)throw new TypeError("Generator is already executing.");for(;u;)try{if(i=1,e&&(o=2&r[0]?e.return:r[0]?e.throw||((o=e.return)&&o.call(e),0):e.next)&&!(o=o.call(e,r[1])).done)return o;switch(e=0,o&&(r=[2&r[0],o.value]),r[0]){case 0:case 1:o=r;break;case 4:return u.label++,{value:r[1],done:!1};case 5:u.label++,e=r[1],r=[0];continue;case 7:r=u.ops.pop(),u.trys.pop();continue;default:if(!(o=(o=u.trys).length>0&&o[o.length-1])&&(6===r[0]||2===r[0])){u=0;continue}if(3===r[0]&&(!o||r[1]>o[0]&&r[1]<o[3])){u.label=r[1];break}if(6===r[0]&&u.label<o[1]){u.label=o[1],o=r;break}if(o&&u.label<o[2]){u.label=o[2],u.ops.push(r);break}o[2]&&u.ops.pop(),u.trys.pop();continue}r=t.call(n,u)}catch(n){r=[6,n],e=0}finally{i=o=0}if(5&r[0])throw r[1];return{value:r[0]?r[1]:void 0,done:!0}}([r,c])}}},j=Object(c.lazy)(function(){return i.e(32).then(i.bind(null,2634))}),_=f.sheets,O=_.Plugin,y=_.path,k=(_.root,_.cell),x=_.tip,C=_.utils,M=_.upLoader,S=_.spread.setSpreadFocus,U=_.sheet._setActiveElement,N=C.showAlert,A=(y.setByPath,k.getActiveCell),z=x.showProgressBar,P=M.upload,T="Attachment",E={baseUrl:"/lizard-api"},I=function(n){function t(i){var e=n.call(this,{name:T,Constructor:t,config:i})||this;return e.dialog=null,e.getAttachmentComponent=function(n){void 0===n&&(n={});var t=e.opts.A;return a.a.createElement(d.a,p({A:t},n))},e.getMenuConfig=function(){return Object(d.b)(p({doUpload:e.doUpload,doCheck:e.doCheck,afterUpload:e.afterUpload,uploadInternalFile:e.uploadInternalFile},e.opts))},e.getMobileMenuConfig=function(){return Object(h.a)(p({doUpload:e.doUpload,doCheck:e.doCheck,afterUpload:e.afterUpload,uploadInternalFile:e.uploadInternalFile},e.opts))},e.doCheck=function(n){var t=n[0],i=e.opts,o=i.beforeUpload,r=i.A;return(!o||!1!==o(r,t))&&!1!==b.a(t)},e.doUpload=function(n,t){return g(e,void 0,void 0,function(){var i,e,o,r,u,c,a,l,s;return w(this,function(f){var d,h,b;return i=n[0],e=this.opts,o=e.A,r=e.uploadUrl,u=o.spread.B().E,c=u.getSelections()[0]||A(u),a=c.row,l=c.col,s=i.name,h=z({sheet:u,row:(d={name:s,cell:{row:a,col:l}}).cell.row,col:d.cell.col}),b=o.uploadConfig,P(i,Object.assign({},b),r).then(function(n){var i=n.url;t(null,p({url:i},d)),h()},function(n){t(n,{}),h()}),[2]})})},e.afterUpload=function(n){return function(t,i){var o=i.name,r=i.url,u=i.cell,c=e.opts.A.spread.B(),a=c.E;if(t)N({title:t});else{var l=u.row,s=u.col,f="attach"===n?r+"?download=1":r;c.actions.setLink(a,{row:l,col:s,text:o,url:f,icon:n})}}},e.uploadInternalFile=function(){var n=e.opts.A.spread.gcSpread,t=n.B();S(n,t,!1),e.importRangeFilePanel.show()},e.handleFileSelect=function(n){var t=e.opts.A.spread.B(),i=t.E,o=i.getSelections()[0]||A(i),r=o.row,u=o.col,c=n[0],a=c.url,l=c.name,s=c.type,f=c.guid,d=a||"/"+s+"/"+f;t.actions.setLink(i,{row:r,col:u,text:l,url:""+location.origin+d,icon:"cloud"}),t.actions.hideLinkDialog(i),e.importRangeFilePanel.hide()},e.setSheetActive=function(){var n=e.opts.A.spread.gcSpread.B();U(n,{ignoreRepaintSelection:!0})},e.opts=i,e.install(),function(n,t){n.isRendered&&t();n.once(m.default.Rendered,t)}(e.opts.A,function(){e.renderFileTreeDialog()}),e}return v(t,n),t.prototype.setLocale=function(n){u.a.setLocaleSync(n)},t.prototype.renderFileTreeDialog=function(){var n=this,t=window.D&&window.D.P||{};s.a.render(a.a.createElement(c.Suspense,{fallback:function(){return null}},a.a.createElement(j,{onSubmit:this.handleFileSelect,service:E,P:t,selectType:"radio",onClose:function(){n.importRangeFilePanel.hide(),n.setSheetActive()},ref:function(t){n.importRangeFilePanel=t}})),this.pluginContainer)},t}(O);t.default=I},2254:function(n,t,i){"use strict";t.a=function(n){var t=window.D&&window.D.P&&window.D.P.accountType;if(t){var i=d[t];return!(i&&i.maxSize<n.size)||(f({title:i.tip}),!1)}return!1},t.c=function(n,t){s(2,"15000"),function(n){e||(t=document.createElement("form"),t.onsubmit=function(n){return n.preventDefault()},t.setAttribute("encType","multipart/form-data"),t.style.position="absolute",t.style.visibility="hidden",t.innerHTML='<input type="file" />',e=t.firstElementChild,document.body.appendChild(t),e=e);var t;e.onchange=n,e.click()}(function(i){var o=i.target.files,r=t.doCheck,u=t.doUpload;if(o.length>0){if(!1===r(o))return;u(o,n)}e.value=""}),c.z.markAsOld()},t.b=function(n,t){s(2,"15001"),t.uploadInternalFile(n)};var e,o=i(0),r=i.n(o),u=i(3),c=i(42),a=u.sheets,l=a.utils,s=a.track,f=l.showAlert,d={personal_free:{tip:""+r()("个人版，单个附件大小上限为50M"),maxSize:52428800},personal_premium:{tip:""+r()("高级版，单个附件大小上限为200M"),maxSize:209715200}}},2629:function(n,t,i){"use strict";var e=i(0),o=i.n(e),r=i(2630),u=i.n(r),c=i(2631),a=i.n(c);o.a.addLocaleResource("en-US",u.a),o.a.addLocaleResource("ja-JP",a.a),o.a.setLocaleSync({en:"en-US",jp:"ja-JP"}[document.documentElement.lang]||document.documentElement.lang||"zh-CN")},2630:function(n,t){n.exports={"选择文件":"Select a file","我的桌面":"My desktop","协作空间":"Collaboration space","个人版，单个附件大小上限为50M":"Maximum size of single attachment is 50M for Personal Edition","高级版，单个附件大小上限为200M":"Maximum size of single attachment is 200M for Premium Edition","附件":"Attachment","登录后才可使用":"Only available after sign-in","石墨文件":"Shimo file","上传附件":"Upload attachment","选择石墨文件":"Select shimo file","登录后可使用":"Available after sign-in","只读模式下不可使用":"Not available in read-only mode"}},2631:function(n,t){n.exports={"选择文件":"ファイルを選択","我的桌面":"デスクトップ","协作空间":"共同スペース","个人版，单个附件大小上限为50M":"パーソナルエディション、添付ファイル1件あたりのサイズ上限は50M","高级版，单个附件大小上限为200M":"アドバンスドエディション、添付ファイル1件あたりのサイズ上限は200M","附件":"添付ファイル","登录后才可使用":"ログインしないと使用できません","石墨文件":null,"上传附件":"添付ファイルをアップロード","选择石墨文件":null,"登录后可使用":"ログインすると使用できます","只读模式下不可使用":"読み取り専用モードでは使用できません"}},2632:function(n,t,i){"use strict";i.d(t,"a",function(){return v});var e,o,r=i(0),u=i.n(r),c=i(1),a=i.n(c),l=i(36),s=i(79),f=i(21),d=i(42),h=i(2254),b=this&&this.__extends||(e=function(n,t){return(e=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(n,t){n.__proto__=t}||function(n,t){for(var i in t)t.hasOwnProperty(i)&&(n[i]=t[i])})(n,t)},function(n,t){function i(){this.constructor=n}e(n,t),n.prototype=null===t?Object.create(t):(i.prototype=t.prototype,new i)}),m=function(n){function t(){var t=null!==n&&n.apply(this,arguments)||this;return t.permissionUpdateKeys=["canEditRange"],t.handleUploadAttachment=function(){Object(h.c)(o.afterUpload("attach"),o)},t.handleInsertInternalFile=function(){Object(h.b)(o.afterUpload("cloud"),o)},t}return b(t,n),Object.defineProperty(t.prototype,"isLoggedIn",{get:function(){var n=this.props.A.permissions.query.shimo.getUserPermission();return Boolean(n&&n.id>0)},enumerable:!0,configurable:!0}),Object.defineProperty(t.prototype,"disabled",{get:function(){var n=this.props,t=n.selection,i=n.isEditing,e=n.permission;return!this.isLoggedIn||i||!e.canEditFirstCell||t.isFormula||t.isCheckBox||t.isDateMentionCell||t.isArrayComputedCell&&!t.isPivotTableExcludedCell},enumerable:!0,configurable:!0}),t.prototype.render=function(){return a.a.createElement(a.a.Fragment,null,a.a.createElement("div",{style:{position:"relative"}},a.a.createElement(f.e,{A:this.props.A,icon:"attachment",text:u()("附件"),disabled:this.disabled,onTap:this.handleUploadAttachment,tip:this.isLoggedIn?null:u()("登录后才可使用")},d.z.visible&&a.a.createElement("span",{className:"badge"}))),a.a.createElement("div",{style:{position:"relative"}},a.a.createElement(f.e,{A:this.props.A,icon:"sm_file",text:u()("石墨文件"),disabled:this.disabled,onTap:this.handleInsertInternalFile,tip:this.isLoggedIn?null:u()("登录后才可使用")},d.z.visible&&a.a.createElement("span",{className:"badge"}))))},t}(l.a),v=function(n){function t(t){var i=n.call(this,t)||this;return i.handleUploadAttachment=function(){if(!i.disabled){var n=i.props,t=n.onSelect,e=n.A.spread.B();e.actions.hideLinkDialog(e.E,!0),Object(h.c)(t("attach"),o)}},i.handleInsertInternalFile=function(){if(!i.disabled){var n=i.props.onSelect;Object(h.b)(n("cloud"),o)}},i}return b(t,n),Object.defineProperty(t.prototype,"disabled",{get:function(){return!(window.D&&window.D.P&&window.D.P.accountType)},enumerable:!0,configurable:!0}),t.prototype.render=function(){return a.a.createElement(a.a.Fragment,null,a.a.createElement("div",{className:"cell-link-suggest-input__attachment cell-link-suggest-input__list-item "+(this.disabled?"cell-link-suggest-input-disabled":""),onClick:this.handleUploadAttachment},u()("上传附件")),a.a.createElement("div",{className:"cell-link-suggest-input__file cell-link-suggest-input__list-item "+(this.disabled?"cell-link-suggest-input-disabled":""),onClick:this.handleInsertInternalFile},u()("选择石墨文件")))},t}(a.a.Component);t.b=function(n){var t;return o=n,{tabList:(t={},t[s.b.insert]=m,t)}}},2633:function(n,t,i){"use strict";t.a=function(n){return o=n,{component:v}};var e,o,r=i(1),u=i.n(r),c=i(244),a=i(243),l=i(0),s=i.n(l),f=i(317),d=i(2254),h=i(3),b=this&&this.__extends||(e=function(n,t){return(e=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(n,t){n.__proto__=t}||function(n,t){for(var i in t)t.hasOwnProperty(i)&&(n[i]=t[i])})(n,t)},function(n,t){function i(){this.constructor=n}e(n,t),n.prototype=null===t?Object.create(t):(i.prototype=t.prototype,new i)}),m=h.sheets.track,v=function(n){function t(){var t=null!==n&&n.apply(this,arguments)||this;return t.selectionUpdateKeys=["isFormula","isCheckbox","isArrayComputedCell","isPivotTableExcludedCell"],t.u=function(){m(2,"18035"),Object(d.c)(o.afterUpload("attach"),o)},t.l=function(){m(2,"18034"),Object(d.b)(o.afterUpload("cloud"),o)},t}return b(t,n),t.prototype.render=function(){return[u.a.createElement(c.a,{key:"online-file"},u.a.createElement(a.a,{disabled:this.disabled,icon:"online-file",text:s()("石墨文件"),onClick:this.l}),!this.isLoggedIn&&u.a.createElement("span",{className:"m-btn-disabled-tip"},s()("登录后可使用"))),u.a.createElement(c.a,{key:"attachment"},u.a.createElement(a.a,{disabled:this.disabled,icon:"attachment",text:s()("附件"),onClick:this.u}),!this.isLoggedIn&&u.a.createElement("span",{className:"m-btn-disabled-tip"},s()("登录后可使用")))]},Object.defineProperty(t.prototype,"isLoggedIn",{get:function(){var n=this.props.A.permissions.query.shimo.getUserPermission();return Boolean(n&&n.accountType)},enumerable:!0,configurable:!0}),Object.defineProperty(t.prototype,"disabled",{get:function(){var n=this.props,t=n.selection,i=n.isEditing,e=n.permission;return!this.isLoggedIn||i||!e.canEditRange||t.isFormula||t.isCheckbox||t.isArrayComputedCell&&!t.isPivotTableExcludedCell},enumerable:!0,configurable:!0}),t}(f.a)}});