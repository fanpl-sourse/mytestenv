(window.webpackJsonplizard_service_file_header=window.webpackJsonplizard_service_file_header||[]).push([[1],{577:function(e,n,t){"use strict";t.r(n),t.d(n,"CollaboratorsButton",function(){return C});var i,a=t(2),o=t(0),p=t.n(o),l=t(1),r=t.n(l),s=t(21),d=t(52),c=t(4),b=t.n(c),u=t(106),g=t.n(u),h=t(850),m=t(20),f=b.a.div(Object(a.__makeTemplateObject)(["\n  display: flex;\n  width: 100%;\n  height: 100%;\n  align-items: center;\n  justify-content: center;\n  > .sm-loading > .loading {\n    margin: 0;\n  }\n"],["\n  display: flex;\n  width: 100%;\n  height: 100%;\n  align-items: center;\n  justify-content: center;\n  > .sm-loading > .loading {\n    margin: 0;\n  }\n"])),v=b.a.div(Object(a.__makeTemplateObject)(["\n  position: fixed;\n  top: 0px;\n  right: 0px;\n  left: 0px;\n  bottom: 0px;\n  background-color: transparent;\n  height: 100%;\n  z-index: 999;\n"],["\n  position: fixed;\n  top: 0px;\n  right: 0px;\n  left: 0px;\n  bottom: 0px;\n  background-color: transparent;\n  height: 100%;\n  z-index: 999;\n"])),x=b()(s.a)(Object(a.__makeTemplateObject)(["\n  position: relative;\n  height: 28px;\n  min-width: 48px;\n  font-weight: normal;\n  padding: 0 12px;\n  margin: 11px 0 !important;\n  color: #888;\n  cursor: ",";\n"],["\n  position: relative;\n  height: 28px;\n  min-width: 48px;\n  font-weight: normal;\n  padding: 0 12px;\n  margin: 11px 0 !important;\n  color: #888;\n  cursor: ",";\n"]),function(e){return e.loading?"wait":"pointer"}),k=b.a.div(Object(a.__makeTemplateObject)(["\n  width: 530px;\n  padding: 0;\n  background: #fff;\n  box-shadow: 0 2px 3px 1px rgba(0, 0, 0, 0.1);\n  border-radius: 2px;\n  position: relative;\n"],["\n  width: 530px;\n  padding: 0;\n  background: #fff;\n  box-shadow: 0 2px 3px 1px rgba(0, 0, 0, 0.1);\n  border-radius: 2px;\n  position: relative;\n"])),C=(i=p.a.Component,Object(a.__extends)(y,i),y.prototype.render=function(){var e=this,n=this.props.online,t=this.state,i=t.isOverlayClicked,a=t.visible,o=t.clickEnable,l=t.collabPanelLoaded;return p.a.createElement(p.a.Fragment,null,p.a.createElement(h.b,{topic:"SharePanel.openCollab",onMessage:function(){return e.onToggleVisibility(!0)}}),i&&a&&n&&p.a.createElement(v,{onClick:function(){return e.changeCollabStatus("hidden")}}),p.a.createElement(d.a,{overlay:p.a.createElement(k,null,this.renderPanel()),destroyPopupOnHide:!0,onVisibleChange:this.onToggleVisibility,placement:"bottomRight",visible:n&&a,showAction:o?["mouseEnter","click"]:["mouseEnter"],hideAction:[i?"":"mouseLeave"],onOverlayClick:this.onOverlayClick,mask:!0,maskClosable:!1,showTip:l,disabled:!n,mouseLeaveDelay:0},p.a.createElement(x,{active:a,type:"primary",size:"s",disabled:!n,loading:!l},r()("协作"))))},y);function y(e){var c=i.call(this,e)||this;return c.LoadableCollabPanel=g()({loader:function(){return Object(a.__awaiter)(c,void 0,void 0,function(){var n=this;return Object(a.__generator)(this,function(e){return[2,t.e(0).then(t.bind(null,954)).then(function(e){return n.setState({collabPanelLoaded:!0}),e})]})})},loading:function(){return p.a.createElement(f,null)}}),c.onToggleVisibility=function(e){void 0===e&&(e=!1),c.props.online&&(e!==c.state.visible&&c.setState({visible:e,clickEnable:!e}),e||c.setState({isOverlayClicked:!1,collabStatus:"initial"}))},c.onOverlayClick=function(){c.state.isOverlayClicked||c.setState({isOverlayClicked:!0})},c.changeCollabStatus=function(e){c.setState({collabStatus:e}),"hidden"===e&&c.onToggleVisibility(!1)},c.handleError=function(e){window.location.reload()},c.renderPanel=function(){var e=c.props,n=e.file,t=e.me,i=e.team,a=e.parentFileGuid,o=n.toJS?n.toJS():n;o.isSpace&&(o.permissions={collaboratorManageable:o.privilege.permission.canModifyCollaborators,adminManageable:o.privilege.permission.canModifyAdmins});var l=!n.isFromSVC&&!n.isSpace,r=Object(m.n)(n)||1<n.collaboratorCount?"normal":"adding",s=t.toJS?t.toJS():t,d=c.LoadableCollabPanel;return p.a.createElement(d,{file:o,me:s,teamId:null==i?void 0:i.id,isEnterpriseAdmin:Object(m.j)(t)||Object(m.k)(t),isEnterpriseVersion:Object(m.l)(t),isDesktopVersion:l,parentFileGuid:a,onClose:function(){return c.changeCollabStatus("hidden")},hideCloseButton:!0,showAddCollab:"adding"==r,zIndex:2e3,onError:c.handleError})},c.state={visible:!1,isOverlayClicked:!1,clickEnable:!1,collabStatus:"initial",collabPanelLoaded:!1},c}n.default=C}}]);
//# sourceMappingURL=collaborators_button.7a3e7ed4.js.map