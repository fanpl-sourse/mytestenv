webpackJsonpSm_name_([14],{1941:function(t,n,i){"use strict";Object.defineProperty(n,"__esModule",{value:!0}),i.d(n,"Events",function(){return e});var r,e,u=i(0),c=i.n(u),o=(i(2721),i(3)),s=i(2255),a=i(2724),f=this&&this.__extends||(r=function(t,n){return(r=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(t,n){t.__proto__=n}||function(t,n){for(var i in n)n.hasOwnProperty(i)&&(t[i]=n[i])})(t,n)},function(t,n){function i(){this.constructor=t}r(t,n),t.prototype=null===n?Object.create(n):(i.prototype=n.prototype,new i)}),h=(o.Editor,o.sheets),l=h.formula,v=(h.root,h.path),d=h.track,b=h.Plugin,m=(v.setByPath,"formulaSidebar"),p="formula";!function(t){t.FORMULA_SIDEBAR_SHOW="formula_sidebar_show",t.FORMULA_SIDEBAR_HIDE="formula_sidebar_hide"}(e||(e={}));var _=function(t){function n(i){var r=t.call(this,{name:m,Constructor:n,config:i})||this;r.show=function(){r.sidebar.show(p),r.emit(e.FORMULA_SIDEBAR_SHOW)},r.hide=function(t){var n=(void 0===t?{}:t).silent;r.sidebar.hide(),!0!==n&&r.emit(e.FORMULA_SIDEBAR_HIDE)},r.onSelect=function(t){var n=r.options.A.spread.B();l.startEditWithFormula(n.E,t),d.trackSetFormula(t,"sidebar")},r.onClose=function(){var t=r.options.onClose;t?t():r.hide()},r.options=i;var u=i.A,o=i.guid,f=i.container,h=new a.a({A:u,onSelect:r.onSelect}),v=[{tag:p,name:c()("插入函数"),component:h}];return r.sidebar=new s.a({A:u,guid:o,appList:v,onClose:r.onClose}),f&&r.render(f),r.install(),r}return f(n,t),n.prototype.setLocale=function(t){c.a.setLocaleSync(t)},n.prototype.render=function(t){this.sidebar.render(t)},n.prototype.destroy=function(){this.removeAllListeners()},n.Events=e,n}(b);n.default=_},2180:function(t,n,i){"use strict";i.d(n,"b",function(){return r}),i.d(n,"a",function(){return e});var r="@TOGGLE_SIDEBAR",e="@SWITCH_TAB"},2255:function(t,n,i){"use strict";var r,e=i(1),u=i.n(e),c=i(6),o=i.n(c),s=i(194),a=(i.n(s),i(18)),f=i(771),h=i(772),l=i(3),v=i(2256),d=i(2257),b=i(2258),m=i(0),p=i.n(m),_=this&&this.__extends||(r=function(t,n){return(r=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(t,n){t.__proto__=n}||function(t,n){for(var i in n)n.hasOwnProperty(i)&&(t[i]=n[i])})(t,n)},function(t,n){function i(){this.constructor=t}r(t,n),t.prototype=null===n?Object.create(n):(i.prototype=n.prototype,new i)}),j=this&&this.__assign||function(){return(j=Object.assign||function(t){for(var n,i=1,r=arguments.length;i<r;i++)for(var e in n=arguments[i])Object.prototype.hasOwnProperty.call(n,e)&&(t[e]=n[e]);return t}).apply(this,arguments)},O=function(t,n){return Object(s.connect)(function(n,i){var r=t.select({isShow:"sidebar.isShow",activeTab:"sidebar.activeTab"},n);return j(j({},r),i)},function(){return n})(b.a)},N="sidebar",S=function(t){function n(i){var r=t.call(this,{name:N,Constructor:n,config:i})||this;return r.store=Object(h.a)({module:Object(f.a)([v.a])}),r.actions=Object(a.a)(r.store.dispatch,d),r.Connected=O(r.store,r.actions),r.options=i,i.container&&r.render(i.container),r.install(),r}return _(n,t),n.prototype.setLocale=function(t){p.a.setLocaleSync(t)},n.prototype.render=function(t){var n=this.store,i=this.Connected;o.a.render(u.a.createElement(s.Provider,{store:n},u.a.createElement(i,j({},j(j({},this.options),{container:t})))),t)},n.prototype.show=function(t){this.isShown=!0,t&&this.setActiveTab(t),this.actions.toggleSidebarAction(!0)},n.prototype.hide=function(){this.isShown=!1,this.actions.toggleSidebarAction(!1)},n.prototype.setActiveTab=function(t){t&&!this.options.appList.some(function(n){return n.tag===t})||this.actions.switchTabAction(t)},n.prototype.S=function(){var t=this.store;return t.select("sidebar.activeTab",t.getState())},n}(l.sheets.Plugin);n.a=S},2256:function(t,n,i){"use strict";var r,e,u=i(2180),c={isShow:[!1,(r={},r[u.b]=function(t,n){return n},r)],activeTab:["",(e={},e[u.a]=function(t,n){return n},e)]};n.a={namespace:"sidebar",reducers:c}},2257:function(t,n,i){"use strict";Object.defineProperty(n,"__esModule",{value:!0}),i.d(n,"toggleSidebarAction",function(){return u}),i.d(n,"switchTabAction",function(){return c});var r=i(7),e=i(2180),u=function(t){return Object(r.c)(e.b,t)},c=function(t){return Object(r.c)(e.a,t)}},2258:function(t,n,i){"use strict";var r,e=i(1),u=i.n(e),c=i(163),o=(i.n(c),i(63)),s=i(3),a=this&&this.__extends||(r=function(t,n){return(r=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(t,n){t.__proto__=n}||function(t,n){for(var i in n)n.hasOwnProperty(i)&&(t[i]=n[i])})(t,n)},function(t,n){function i(){this.constructor=t}r(t,n),t.prototype=null===n?Object.create(n):(i.prototype=n.prototype,new i)}),f=s.sheets.utils.preventWheelBack,h=function(t){function n(n){var i=t.call(this,n)||this;return i.onClose=function(){i.setState({shouldUpdateCnt:!1}),i.props.toggleSidebarAction(!1),i.props.switchTabAction(null),i.props.appList.forEach(function(t){var n=t.component;n.destory&&n.destory()}),o.default.isFunction(i.props.onClose)&&i.props.onClose()},i.state={shouldUpdateCnt:!1,tabListLength:{}},i}return a(n,t),n.prototype.componentDidMount=function(){var t=this;this.props.appList.forEach(function(n){var i=n.tag,r=n.component,e=t.refs.smSidebarList.querySelector(".sm-sidebar-applist-"+i);e&&r.render(e,{getListLength:t.getListLength.bind(t,i)}),i===t.props.activeTab&&r.show()}),f(this.refs.smSidebarList,!0)},n.prototype.getListLength=function(t,n){var i=this.state.tabListLength;i[t]=n,this.setState({tabListLength:i})},n.prototype.componentWillReceiveProps=function(t){var n=this;this.props.activeTab!==t.activeTab&&(o.default.isFunction(this.props.onTabSwitch)&&this.props.onTabSwitch(this.props.activeTab,t.activeTab),t.appList.forEach(function(i){var r=i.tag,e=i.component;r===n.props.activeTab&&e.hide(),r===t.activeTab&&e.show()})),this.props.isShow&&!t.isShow&&this.onClose(),!this.props.isShow&&t.isShow&&t.appList.forEach(function(t){var n=t.component;n.reload&&n.reload()})},n.prototype.onClick=function(t){t!==this.props.activeTab&&(o.default.isFunction(this.props.onTabSwitch)?this.props.onTabSwitch(this.props.activeTab,t):this.props.switchTabAction(t))},n.prototype.render=function(){var t=this,n=this.props,i=n.activeTab,r=n.isShow,e=n.appList,o=void 0===e?[]:e,s=this.state.tabListLength;return u.a.createElement("div",{className:Object(c.className)({"sm-sheet-editor-sidebar":!0,show:r}),ref:"smSidebarList"},u.a.createElement("div",{className:"doc-history-title spreadsheet"},o.map(function(n){var r=n.tag,e=n.name,c=i===r;return u.a.createElement("span",{key:r,className:"s-title-text s-title-text-"+r+" "+(c?"active":""),onClick:function(){return t.onClick(r)}},e+" "+(null!=s[r]?"("+s[r]+")":""))}),u.a.createElement("span",{className:"icon-close hicon doc-sidebar-close",onClick:this.onClose.bind(this)})),o.map(function(t){var n=t.tag;return u.a.createElement("div",{key:n,className:"sm-sidebar sm-sidebar-applist-"+n+" "+(n!==i?"hide":"")})}))},n}(e.Component);n.a=h},2721:function(t,n,i){"use strict";var r=i(0),e=i.n(r),u=i(2722),c=i.n(u),o=i(2723),s=i.n(o);e.a.addLocaleResource("en-US",c.a),e.a.addLocaleResource("ja-JP",s.a),e.a.setLocaleSync({en:"en-US",jp:"ja-JP"}[document.documentElement.lang]||document.documentElement.lang||"zh-CN")},2722:function(t,n){t.exports={"搜索":"Search","无搜索结果":"No search results","插入函数":"Insert function"}},2723:function(t,n){t.exports={"搜索":"検索","无搜索结果":"検索結果はありません","插入函数":"関数を挿入"}},2724:function(t,n,i){"use strict";var r,e=i(0),u=i.n(e),c=i(1),o=i.n(c),s=i(6),a=i.n(s),f=i(31),h=i.n(f),l=i(3),v=i(2725),d=(i.n(v),this&&this.__extends||(r=function(t,n){return(r=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(t,n){t.__proto__=n}||function(t,n){for(var i in n)n.hasOwnProperty(i)&&(t[i]=n[i])})(t,n)},function(t,n){function i(){this.constructor=t}r(t,n),t.prototype=null===n?Object.create(n):(i.prototype=n.prototype,new i)})),b=this&&this.__assign||function(){return(b=Object.assign||function(t){for(var n,i=1,r=arguments.length;i<r;i++)for(var e in n=arguments[i])Object.prototype.hasOwnProperty.call(n,e)&&(t[e]=n[e]);return t}).apply(this,arguments)},m=l.sheets.spread.focusActiveSheet,p=function(t){var n=t.name,i=t.detail,r=t.onSelect;return o.a.createElement("li",{className:"fp-list__item",onClick:function(){return r(n)}},o.a.createElement("div",{className:"fp-list__item-name"},n),o.a.createElement("p",{className:"fp-weak-text",dangerouslySetInnerHTML:{__html:i}}))},_=function(t){function n(n){var i=t.call(this,n)||this;return i.onSearchFocus=function(){i.props.A.spread.B().E.isEditing()||m(null)},i.onSearchChange=function(t){"string"!=typeof t&&(t=t.target.value||""),i.setState({searchText:t}),t?i.searchFormulaByKey(t):i.searchFormulasbyCatagory(i.state.activeCatagory)},i.onClearSearch=function(){i.onSearchChange("")},i.state={open:!1,searchText:"",activeCatagory:"all",formulaNames:Object(v.searchByNameOrDetail)("")},i}return d(n,t),n.prototype.searchFormulasbyCatagory=function(t){void 0===t&&(t="hot");var n=Object(v.formulaGroups)(t);this.setState({formulaNames:n})},n.prototype.searchFormulaByKey=function(t){void 0===t&&(t="");var n=Object(v.searchByNameOrDetail)(t.trim());this.setState({formulaNames:n})},n.prototype.render=function(){return this.state.open?o.a.createElement("div",{className:"fp-formula-panel"},this.renderSearchBar(),this.renderList()):null},n.prototype.renderSearchBar=function(){var t=this.state.searchText;return o.a.createElement("div",{className:"fp-search"},o.a.createElement("span",{className:"team-sprite team-icon-search"}),o.a.createElement("input",{className:"form-control list-item-input sm-input-default fp-search__input",placeholder:u()("搜索"),value:t,onFocus:this.onSearchFocus,onChange:this.onSearchChange}),o.a.createElement("span",{className:h()({"fp-pointer":!0,"team-sprite":!0,"team-icon-delete":!0,"fp--hide":0===t.length}),onClick:this.onClearSearch}))},n.prototype.renderList=function(){var t=this.props.onSelect,n=this.state.formulaNames;return 0===n.length?o.a.createElement("div",{className:"fp-list"},o.a.createElement("div",{className:"fp-weak-text fp-list__empty"},u()("无搜索结果"))):o.a.createElement("ul",{className:"fp-list"},n.map(function(n){return o.a.createElement(p,{key:n.name,name:n.name,detail:n.description,onSelect:t})}))},n}(o.a.Component),j=function(){function t(t){this.options=t}return t.prototype.render=function(t){var n=this;a.a.render(o.a.createElement(_,b({},this.options,{ref:function(t){return n.formulaList=t}})),t)},t.prototype.show=function(){this.formulaList&&this.formulaList.setState({open:!0})},t.prototype.hide=function(){this.formulaList&&this.formulaList.setState({open:!1})},t}();n.a=j},2725:function(t,n,i){Object.defineProperty(n,"__esModule",{value:!0});var r=Object.assign||function(t){for(var n=1;n<arguments.length;n++){var i=arguments[n];for(var r in i)Object.prototype.hasOwnProperty.call(i,r)&&(t[r]=i[r])}return t};n.searchByNameOrDetail=function(t){var n=a();return""===t?n:n.filter(function(n){return(0,c.default)(n.name,t.toUpperCase())||(0,c.default)(n.description,t)}).map(function(n){if((0,c.default)(n.description,t)){var i=n.description.replace(t,"<span>"+t+"</span>");return r({},n,{description:i})}return n})},n.formulaGroups=function(){var t=arguments.length>0&&void 0!==arguments[0]?arguments[0]:"all",n=a(),i=f();if("all"===t)return n;if("hot"===t)return["SUM","AVERAGE","COUNT","MAX","MIN","IF","SIN","SUMIF"];if(i.hasOwnProperty(t))return i[t]};var e=function(t){if(t&&t.__esModule)return t;var n={};if(null!=t)for(var i in t)Object.prototype.hasOwnProperty.call(t,i)&&(n[i]=t[i]);return n.default=t,n}(i(3)),u=o(i(2726)),c=o(i(348));function o(t){return t&&t.__esModule?t:{default:t}}var s=e.sheets.Core,a=function(){var t=s.Spread.Common._getBuiltInFunctionsResource();return Object.keys(t).map(function(n){return r({name:n},t[n])})},f=function(){var t=s.Spread.Common._getBuiltInFunctionsResource(),n=Object.keys(t);return(0,u.default)(n,function(n){return t[n][0]})}},2726:function(t,n,i){var r=i(485),e=Object.prototype.hasOwnProperty,u=r(function(t,n,i){e.call(t,i)?t[i].push(n):t[i]=[n]});t.exports=u}});