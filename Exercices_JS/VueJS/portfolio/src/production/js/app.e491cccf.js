(function(t){function e(e){for(var n,s,d=e[0],r=e[1],l=e[2],u=0,f=[];u<d.length;u++)s=d[u],Object.prototype.hasOwnProperty.call(i,s)&&i[s]&&f.push(i[s][0]),i[s]=0;for(n in r)Object.prototype.hasOwnProperty.call(r,n)&&(t[n]=r[n]);a&&a(e);while(f.length)f.shift()();return c.push.apply(c,l||[]),o()}function o(){for(var t,e=0;e<c.length;e++){for(var o=c[e],n=!0,d=1;d<o.length;d++){var r=o[d];0!==i[r]&&(n=!1)}n&&(c.splice(e--,1),t=s(s.s=o[0]))}return t}var n={},i={app:0},c=[];function s(e){if(n[e])return n[e].exports;var o=n[e]={i:e,l:!1,exports:{}};return t[e].call(o.exports,o,o.exports,s),o.l=!0,o.exports}s.m=t,s.c=n,s.d=function(t,e,o){s.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:o})},s.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},s.t=function(t,e){if(1&e&&(t=s(t)),8&e)return t;if(4&e&&"object"===typeof t&&t&&t.__esModule)return t;var o=Object.create(null);if(s.r(o),Object.defineProperty(o,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var n in t)s.d(o,n,function(e){return t[e]}.bind(null,n));return o},s.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return s.d(e,"a",e),e},s.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},s.p="/";var d=window["webpackJsonp"]=window["webpackJsonp"]||[],r=d.push.bind(d);d.push=e,d=d.slice();for(var l=0;l<d.length;l++)e(d[l]);var a=r;c.push([0,"chunk-vendors"]),o()})({0:function(t,e,o){t.exports=o("56d7")},"22e2":function(t,e,o){"use strict";o("3f95")},"3f95":function(t,e,o){},"44cb":function(t,e,o){},"56d7":function(t,e,o){"use strict";o.r(e);o("e260"),o("e6cf"),o("cca6"),o("a79d");var n=o("7a23"),i={id:"app"},c={class:"title"},s={class:"container"},d={class:"box"},r={class:"todoList"},l={class:"footer"},a={class:"copyright"};function u(t,e,o,u,f,p){var b=Object(n["k"])("NewTodo"),h=Object(n["k"])("Todo"),O=Object(n["k"])("Footer");return Object(n["g"])(),Object(n["c"])("div",i,[Object(n["d"])("div",c,Object(n["l"])(f.title),1),Object(n["d"])("div",s,[Object(n["d"])("div",d,[Object(n["e"])(b,{onAddTodo:p.addToList},null,8,["onAddTodo"]),Object(n["d"])("ul",r,[Object(n["e"])(h,{todos:f.showTodos||f.todos,class:"todos",onDestroyTodo:p.destroyTodo},null,8,["todos","onDestroyTodo"])]),Object(n["d"])("div",l,[Object(n["e"])(O,{onShow:p.show,onClearCompleted:p.clearCompleted,itemsLeft:p.itemsLeft,todos:f.showTodos||f.todos},null,8,["onShow","onClearCompleted","itemsLeft","todos"])])])]),Object(n["d"])("div",a,Object(n["l"])(p.copyright),1)])}o("e9c4"),o("4de4"),o("d3b7"),o("a434");var f={class:"container"},p=["onDblclick"],b=["onUpdate:modelValue"],h=["value"],O={class:"date"},j=["onClick"];function m(t,e,o,i,c,s){return Object(n["g"])(),Object(n["c"])("div",f,[(Object(n["g"])(!0),Object(n["c"])(n["a"],null,Object(n["j"])(o.todos,(function(t){return Object(n["g"])(),Object(n["c"])("li",{class:"todo",key:t.index,onDblclick:function(e){return s.startEdit(t)}},[Object(n["p"])(Object(n["d"])("input",{type:"checkbox",class:Object(n["f"])({done:t.isDone}),"onUpdate:modelValue":function(e){return t.isDone=e}},null,10,b),[[n["m"],t.isDone]]),Object(n["d"])("label",{for:"todoText",id:"labelText",class:Object(n["f"])({done:t.isDone,editing:t===c.editing})},Object(n["l"])(t.text),3),Object(n["d"])("input",{type:"text",id:"todoText",value:t.text,class:Object(n["f"])({editing:t===c.editing}),onKeyup:[e[0]||(e[0]=Object(n["q"])((function(){return s.cancelEdit&&s.cancelEdit.apply(s,arguments)}),["esc"])),e[2]||(e[2]=Object(n["q"])((function(){return s.finishEdit&&s.finishEdit.apply(s,arguments)}),["enter"]))],onBlur:e[1]||(e[1]=function(){return s.finishEdit&&s.finishEdit.apply(s,arguments)}),autofocus:""},null,42,h),Object(n["d"])("span",O,Object(n["l"])(t.date),1),Object(n["d"])("span",{class:"material-icons",id:"delete",onClick:function(e){return s.destroy(t)}}," delete ",8,j)],40,p)})),128))])}var v={name:"Todo",props:["todos"],data:function(){return{editing:null}},computed:{},methods:{startEdit:function(t){this.editing=t},finishEdit:function(t){if(this.editing){var e=t.target;this.editing.text=e.value,this.editing=null}},cancelEdit:function(){this.editing=null},destroy:function(t){this.$emit("destroy-todo",{todo:t})}}},g=(o("22e2"),o("6b0d")),w=o.n(g);const y=w()(v,[["render",m],["__scopeId","data-v-12e76e0c"]]);var D=y,T={class:"container"};function x(t,e,o,i,c,s){return Object(n["g"])(),Object(n["c"])("div",T,[Object(n["p"])(Object(n["d"])("input",{type:"text",id:"text",placeholder:"Add new task...",onKeyup:e[0]||(e[0]=Object(n["q"])((function(){return s.addTodo&&s.addTodo.apply(s,arguments)}),["enter"])),"onUpdate:modelValue":e[1]||(e[1]=function(t){return c.todo.text=t})},null,544),[[n["n"],c.todo.text]])])}var C={name:"NewTodo",data:function(){return{todo:{text:"",isDone:!1,date:(new Date).toLocaleDateString()}}},methods:{addTodo:function(){this.$emit("add-todo",this.todo),this.todo={text:"",isDone:!1,date:(new Date).toLocaleDateString()}}}};o("e802");const k=w()(C,[["render",x],["__scopeId","data-v-58acf934"]]);var A=k,L={class:"container"},S={class:"left"},_={class:"select"};function E(t,e,o,i,c,s){return Object(n["g"])(),Object(n["c"])("div",L,[Object(n["d"])("span",S,Object(n["l"])(o.itemsLeft)+" items left",1),Object(n["d"])("div",_,[Object(n["d"])("span",{class:Object(n["f"])({selected:"All"==c.selection}),onClick:e[0]||(e[0]=function(t){return s.show("All")})},"All",2),Object(n["d"])("span",{class:Object(n["f"])({selected:"Active"==c.selection}),onClick:e[1]||(e[1]=function(t){return s.show("Active")})},"Active",2),Object(n["d"])("span",{class:Object(n["f"])({selected:"Completed"==c.selection}),onClick:e[2]||(e[2]=function(t){return s.show("Completed")})}," Completed ",2)]),Object(n["d"])("div",null,[Object(n["p"])(Object(n["d"])("span",{class:"clear",onClick:e[3]||(e[3]=function(){return s.clearCompleted&&s.clearCompleted.apply(s,arguments)})},"Clear completed",512),[[n["o"],s.completedLeft.length]])])])}var P={data:function(){return{selection:"All"}},props:["itemsLeft","todos"],computed:{completedLeft:function(){return this.todos.filter((function(t){return t.isDone}))}},methods:{show:function(t){this.$emit("show",{selection:t}),this.selection=t},clearCompleted:function(){"Completed"==this.selection&&(this.selection="All"),this.$emit("clear-completed")}}};o("b5e6");const I=w()(P,[["render",E],["__scopeId","data-v-b8cd0124"]]);var N=I,J={name:"App",components:{Todo:D,NewTodo:A,Footer:N},data:function(){return{title:"Todos!",todos:JSON.parse(localStorage.getItem("todos"))||[{text:"third thing",isDone:!1,date:this.newDate(3)},{text:"second thing",isDone:!1,date:this.newDate(5)},{text:"first thing",isDone:!0,date:this.newDate(12)}],showTodos:this.todos,selection:"All"}},watch:{todos:{deep:!0,handler:function(t){localStorage.setItem("todos",JSON.stringify(t))}}},computed:{copyright:function(){var t=(new Date).getFullYear();return"Copyright © ".concat(t)},itemsLeft:function(){return this.todos.filter((function(t){return 0==t.isDone})).length}},methods:{addToList:function(t){var e=t;this.todos.unshift(e)},newDate:function(t){var e=Date.now(),o=24*t*3600*1e3;return new Date(e-o).toLocaleDateString()},destroyTodo:function(t){var e=this.todos.indexOf(t.todo);this.todos.splice(e,1),this.todo=""},show:function(t){switch(this.selection=t.selection||t,this.selection){case"Active":this.showTodos=this.todos.filter((function(t){return!1===t.isDone}));break;case"Completed":this.showTodos=this.todos.filter((function(t){return!0===t.isDone}));break;default:this.showTodos=this.todos;break}},clearCompleted:function(){this.todos=this.todos.filter((function(t){return 0==t.isDone})),this.show("All")}}};o("dd00");const M=w()(J,[["render",u]]);var $=M;Object(n["b"])($).mount("#app")},b5e6:function(t,e,o){"use strict";o("44cb")},bd58:function(t,e,o){},dd00:function(t,e,o){"use strict";o("f83b")},e802:function(t,e,o){"use strict";o("bd58")},f83b:function(t,e,o){}});
//# sourceMappingURL=app.e491cccf.js.map