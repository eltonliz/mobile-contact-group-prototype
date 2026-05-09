# -*- coding: utf-8 -*-
import re

with open("/Users/elton/Desktop/AI主播稿+通讯录副本/移动端通讯录与群管理工作台原型.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add WeChat green CSS variable
content = content.replace(
    ":root {\n  --primary: #26C7A5;",
    ":root {\n  --wechat-green: #07C160;\n  --primary: #26C7A5;",
    1
)

# 2. Add new CSS styles before closing </style>
new_css = """
/* WeChat Message List */
.msg-item { display: flex; align-items: center; padding: 12px 16px; border-bottom: 0.5px solid var(--border); cursor: pointer; transition: background 0.15s; background: var(--bg-card); }
.msg-item:active { background: #F5F5F5; }
.msg-item-avatar { width: 44px; height: 44px; border-radius: 6px; display: flex; align-items: center; justify-content: center; font-size: 18px; font-weight: 600; color: white; flex-shrink: 0; margin-right: 12px; }
.msg-item-content { flex: 1; min-width: 0; }
.msg-item-name { font-size: 15px; font-weight: 500; color: var(--text-primary); line-height: 1.3; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.msg-item-preview { font-size: 12px; color: var(--text-tertiary); margin-top: 3px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.msg-item-meta { flex-shrink: 0; text-align: right; margin-left: 8px; }
.msg-item-time { font-size: 11px; color: var(--text-tertiary); }
.msg-item-badge { display: inline-flex; min-width: 16px; height: 16px; background: var(--danger); color: white; font-size: 10px; border-radius: 8px; align-items: center; justify-content: center; padding: 0 4px; font-weight: 600; margin-top: 4px; }
/* Contacts */
.contact-shortcuts { background: var(--bg-card); }
.shortcut-item { display: flex; align-items: center; padding: 12px 16px; border-bottom: 0.5px solid var(--border); cursor: pointer; transition: background 0.15s; }
.shortcut-item:active { background: #F5F5F5; }
.shortcut-icon { width: 40px; height: 40px; border-radius: 6px; display: flex; align-items: center; justify-content: center; font-size: 20px; margin-right: 12px; flex-shrink: 0; }
.shortcut-icon.new-friend { background: #F09B37; color: white; }
.shortcut-icon.my-group { background: var(--wechat-green); color: white; }
.shortcut-label { flex: 1; font-size: 15px; color: var(--text-primary); }
.shortcut-badge { background: var(--danger); color: white; font-size: 10px; padding: 1px 6px; border-radius: 8px; margin-right: 8px; }
.contact-section { background: var(--bg-card); }
.section-header { padding: 6px 16px; font-size: 13px; font-weight: 600; color: var(--text-tertiary); background: var(--bg-page); }
.contact-item { display: flex; align-items: center; padding: 10px 16px; border-bottom: 0.5px solid var(--border); cursor: pointer; transition: background 0.15s; }
.contact-item:active { background: #F5F5F5; }
.contact-item:last-child { border-bottom: none; }
.contact-avatar { width: 40px; height: 40px; border-radius: 6px; display: flex; align-items: center; justify-content: center; font-size: 16px; font-weight: 600; color: white; flex-shrink: 0; margin-right: 12px; }
.contact-name { flex: 1; font-size: 15px; color: var(--text-primary); }
.alpha-index { position: absolute; right: 2px; top: 50%; transform: translateY(-50%); z-index: 50; display: flex; flex-direction: column; align-items: center; }
.alpha-index span { font-size: 10px; color: var(--text-tertiary); padding: 1px 4px; cursor: pointer; line-height: 1.3; }
.alpha-index span:active { color: var(--wechat-green); font-weight: 700; }
/* Friend Detail */
.friend-info-card { background: var(--bg-card); padding: 20px 16px; display: flex; align-items: flex-start; gap: 14px; }
.friend-avatar-lg { width: 56px; height: 56px; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 24px; font-weight: 600; color: white; flex-shrink: 0; }
.friend-basic { flex: 1; }
.friend-name-lg { font-size: 18px; font-weight: 700; line-height: 1.3; }
.friend-remark { font-size: 13px; color: var(--text-tertiary); margin-top: 2px; }
.friend-detail-row { display: flex; align-items: center; padding: 12px 16px; background: var(--bg-card); border-bottom: 0.5px solid var(--border); font-size: 14px; }
.friend-detail-row:last-child { border-bottom: none; }
.friend-detail-label { color: var(--text-secondary); width: 60px; flex-shrink: 0; }
.friend-detail-value { flex: 1; color: var(--text-primary); }
.friend-actions { display: flex; gap: 12px; padding: 20px 16px; }
.friend-actions .action-btn { flex: 1; padding: 10px; border-radius: 8px; font-size: 14px; font-weight: 500; cursor: pointer; text-align: center; border: none; font-family: inherit; transition: all 0.15s; }
.friend-actions .action-btn:active { transform: scale(0.97); }
.friend-actions .action-btn.primary { background: var(--wechat-green); color: white; }
.friend-actions .action-btn.outline { background: var(--bg-card); color: var(--text-primary); border: 0.5px solid var(--border); }
/* Friend Request */
.friend-request-item { display: flex; align-items: center; padding: 12px 16px; background: var(--bg-card); border-bottom: 0.5px solid var(--border); }
.friend-request-avatar { width: 40px; height: 40px; border-radius: 6px; display: flex; align-items: center; justify-content: center; font-size: 16px; font-weight: 600; color: white; flex-shrink: 0; margin-right: 12px; }
.friend-request-info { flex: 1; }
.friend-request-name { font-size: 15px; font-weight: 500; }
.friend-request-msg { font-size: 12px; color: var(--text-tertiary); margin-top: 2px; }
/* Add Menu */
.add-menu { position: absolute; top: calc(var(--status-h) + var(--nav-h) - 4px); right: 12px; background: #4C4C4C; border-radius: 6px; z-index: 180; padding: 4px 0; min-width: 140px; display: none; box-shadow: 0 4px 12px rgba(0,0,0,0.3); }
.add-menu.show { display: block; }
.add-menu-item { display: flex; align-items: center; gap: 10px; padding: 10px 16px; color: white; font-size: 14px; cursor: pointer; transition: background 0.15s; }
.add-menu-item:active { background: rgba(255,255,255,0.1); }
.add-menu-item .menu-icon { font-size: 18px; }
.add-menu::before { content: ''; position: absolute; top: -6px; right: 16px; width: 0; height: 0; border-left: 6px solid transparent; border-right: 6px solid transparent; border-bottom: 6px solid #4C4C4C; }
/* Confirm Dialog */
.confirm-dialog { position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.5); z-index: 250; display: none; align-items: center; justify-content: center; }
.confirm-dialog.show { display: flex; }
.confirm-box { background: var(--bg-card); border-radius: 12px; width: 270px; overflow: hidden; }
.confirm-title { padding: 20px 16px 8px; font-size: 16px; font-weight: 600; text-align: center; }
.confirm-body { padding: 4px 16px 20px; font-size: 13px; color: var(--text-secondary); text-align: center; line-height: 1.5; }
.confirm-btns { display: flex; border-top: 0.5px solid var(--border); }
.confirm-btn { flex: 1; padding: 12px; font-size: 16px; text-align: center; cursor: pointer; border: none; background: none; font-family: inherit; }
.confirm-btn:active { background: #F5F5F5; }
.confirm-btn.cancel { color: var(--text-secondary); border-right: 0.5px solid var(--border); }
.confirm-btn.ok { color: var(--wechat-green); font-weight: 500; }
/* Group Detail */
.group-detail-section { background: var(--bg-card); margin-bottom: 8px; }
.group-detail-row { display: flex; align-items: center; padding: 14px 16px; border-bottom: 0.5px solid var(--border); font-size: 14px; cursor: pointer; }
.group-detail-row:last-child { border-bottom: none; }
.group-detail-row:active { background: #F5F5F5; }
.group-detail-label { flex: 1; color: var(--text-primary); }
.group-detail-value { color: var(--text-tertiary); font-size: 13px; margin-right: 8px; }
.group-detail-arrow { color: var(--text-tertiary); font-size: 14px; }
/* WeChat btn */
.btn-wechat { background: var(--wechat-green); color: white; border: none; }
.btn-wechat:hover { background: #06ad56; }
"""
content = content.replace("</style>\n</head>", new_css + "\n</style>\n</head>", 1)

# 3. Replace home page content
old_home_start = '    <div class="page active" id="page-home">'
old_home_end = '      <div style="height:20px"></div>\n    </div>'
home_start_idx = content.find(old_home_start)
home_end_idx = content.find(old_home_end, home_start_idx) + len(old_home_end)
old_home = content[home_start_idx:home_end_idx]
new_home = '    <div class="page active" id="page-home">\n      <div class="search-bar">\n        <input class="search-input" placeholder="搜索" id="globalSearch" oninput="handleGlobalSearch(this.value)">\n      </div>\n      <div id="msgListPage"></div>\n      <div style="height:20px"></div>\n    </div>'
content = content[:home_start_idx] + new_home + content[home_end_idx:]

# 4. Replace customer page with contacts page
old_cust_start = '    <div class="page" id="page-customer">'
old_cust_end_marker = '      <div style="height:20px"></div>\n    </div>\n\n    <div class="page" id="page-mine">'
cust_start_idx = content.find(old_cust_start)
cust_end_idx = content.find(old_cust_end_marker, cust_start_idx)
old_cust = content[cust_start_idx:cust_end_idx] + '      <div style="height:20px"></div>\n    </div>'
new_contacts = '    <div class="page" id="page-contacts">\n      <div class="search-bar" style="display:flex;align-items:center;gap:8px;padding:8px 12px;">\n        <input class="search-input" placeholder="请输入您要搜索的关键字" id="contactSearch" oninput="handleContactSearch(this.value)" style="flex:1">\n        <div style="width:32px;height:32px;display:flex;align-items:center;justify-content:center;cursor:pointer;font-size:20px;color:var(--text-primary);flex-shrink:0" onclick="toggleAddMenu()">\uff0b</div>\n      </div>\n      <div class="contact-shortcuts">\n        <div class="shortcut-item" onclick="showNewFriends()">\n          <div class="shortcut-icon new-friend">\U0001f7e2</div>\n          <span class="shortcut-label">新的朋友</span>\n          <span class="shortcut-badge" id="newFriendBadge">3</span>\n          <span style="color:var(--text-tertiary);font-size:14px">\u203a</span>\n        </div>\n        <div class="shortcut-item" onclick="showMyGroups()">\n          <div class="shortcut-icon my-group">\U0001f465</div>\n          <span class="shortcut-label">我的群聊</span>\n          <span style="color:var(--text-tertiary);font-size:14px">\u203a</span>\n        </div>\n      </div>\n      <div id="contactList" style="position:relative;"></div>\n      <div class="alpha-index" id="alphaIndex"></div>\n      <div style="height:20px"></div>\n    </div>'
content = content[:cust_start_idx] + new_contacts + content[cust_start_idx + len(old_cust):]

# 5. Replace tab bar
old_tab_start = '  <div class="tab-bar" id="tabBar">'
old_tab_end = '  </div>\n\n  <div class="sub-page"'
tab_start_idx = content.find(old_tab_start)
tab_end_idx = content.find(old_tab_end, tab_start_idx) + len('  </div>')
old_tab = content[tab_start_idx:tab_end_idx]
new_tab = '  <div class="tab-bar" id="tabBar">\n    <div class="tab-item active" onclick="switchTab(\'home\')">\n      <div class="tab-icon-wrap"><span class="tab-icon">\U0001f4ac</span><span class="badge" id="homeBadge" style="display:none">0</span></div>\n      <span class="tab-label">消息</span>\n    </div>\n    <div class="tab-item" onclick="switchTab(\'contacts\')">\n      <div class="tab-icon-wrap"><span class="tab-icon">\U0001f4c7</span></div>\n      <span class="tab-label">通讯录</span>\n    </div>\n    <div class="tab-item" onclick="switchTab(\'group\')">\n      <div class="tab-icon-wrap"><span class="tab-icon">\U0001f465</span><span class="badge" id="groupBadge" style="display:none">0</span></div>\n      <span class="tab-label">群管理</span>\n    </div>\n    <div class="tab-item" onclick="switchTab(\'mine\')">\n      <div class="tab-icon-wrap"><span class="tab-icon">\u2699\ufe0f</span></div>\n      <span class="tab-label">我的</span>\n    </div>\n  </div>\n  <div class="add-menu" id="addMenu">\n    <div class="add-menu-item" onclick="showAddFriend()"><span class="menu-icon">\U0001f464</span>添加好友</div>\n    <div class="add-menu-item" onclick="showCreateGroup()"><span class="menu-icon">\U0001f465</span>创建群聊</div>\n  </div>'
content = content[:tab_start_idx] + new_tab + content[tab_start_idx + len(old_tab):]

# 6. Add confirm dialog before toast
content = content.replace(
    '  <div class="toast" id="toast"></div>',
    '  <div class="confirm-dialog" id="confirmDialog">\n    <div class="confirm-box">\n      <div class="confirm-title" id="confirmTitle">提示</div>\n      <div class="confirm-body" id="confirmBody"></div>\n      <div class="confirm-btns">\n        <button class="confirm-btn cancel" onclick="closeConfirm()">取消</button>\n        <button class="confirm-btn ok" id="confirmOk">确定</button>\n      </div>\n    </div>\n  </div>\n  <div class="toast" id="toast"></div>',
    1
)

# 7. Replace nav title
content = content.replace(
    '<div class="title" id="navTitle">首页</div>',
    '<div class="title" id="navTitle">消息</div>',
    1
)

# 8. Replace switchTab function
content = content.replace(
    "var pageMap = {home:'page-home',group:'page-group',customer:'page-customer',mine:'page-mine'};",
    "var pageMap = {home:'page-home',contacts:'page-contacts',group:'page-group',mine:'page-mine'};",
    1
)
content = content.replace(
    "var tabIndex = {home:0,group:1,customer:2,mine:3};",
    "var tabIndex = {home:0,contacts:1,group:2,mine:3};",
    1
)
content = content.replace(
    "var titles = {home:'首页',group:'群管理',customer:'客户',mine:'我的'};",
    "var titles = {home:'消息',contacts:'通讯录',group:'群管理',mine:'我的'};",
    1
)

# Add closeAddMenu() to switchTab
content = content.replace(
    "document.getElementById('pageContainer').scrollTop = 0;\n}",
    "document.getElementById('pageContainer').scrollTop = 0;\n  closeAddMenu();\n}",
    1
)

# 9. Replace renderAll
content = content.replace(
    "function renderAll() {\n  renderDataOverview(); renderQuickActions(); renderTasks(); renderActivities();\n  renderGroupTabs(); renderGroupList(); renderCustomerTabs(); renderCustomerList();\n  renderMinePage(); updateBadges();\n}",
    "function renderAll() {\n  renderMessageList(); renderContactList(); renderGroupTabs(); renderGroupList();\n  renderMinePage(); updateBadges(); updateNewFriendBadge();\n}",
    1
)

# 10. Replace updateBadges
content = content.replace(
    "var dc = PENDING_TASKS.filter(function(t){return t.type==='danger'}).length;\n  var cb = document.getElementById('customerBadge');\n  if (dc>0) { cb.style.display='flex'; cb.textContent=dc; } else { cb.style.display='none'; }",
    "var hb = document.getElementById('homeBadge');\n  var totalUnread = MESSAGE_LIST.reduce(function(sum,m){return sum+m.badge},0);\n  if(totalUnread>0) { hb.style.display='flex'; hb.textContent=totalUnread; } else { hb.style.display='none'; }",
    1
)

# 11. Replace handleGlobalSearch
content = content.replace(
    "function handleGlobalSearch(v) { if (!v.trim()) return; showToast('搜索：'+v); }",
    "function handleGlobalSearch(v) { renderMessageList(); }",
    1
)

# 12. Tab active color to wechat-green
content = content.replace(
    ".tab-item.active { color: var(--primary); }",
    ".tab-item.active { color: var(--wechat-green); }",
    1
)

# 13. Update PRD annotation tabKeys
content = content.replace(
    "var tabKeys = ['home','group','customer','mine'];",
    "var tabKeys = ['home','contacts','group','mine'];",
    1
)

# 14. Update PRD annotation page visibility
content = content.replace(
    "if (ann.page === 'customer') return activeTab === 'customer';",
    "if (ann.page === 'contacts') return activeTab === 'contacts';",
    1
)

# 15. Add new data and functions before Init section
new_js = r"""
/* ========== WeChat Contacts Data ========== */

var CONTACTS = [
  {id:'ct1',name:'陈世敏',pinyin:'C',phone:'130 3325 8577',region:'广东省广州市天河区',remark:'',avatar:'blue'},
  {id:'ct2',name:'程娉婷',pinyin:'C',phone:'139 8832 7766',region:'广东省深圳市南山区',remark:'',avatar:'green'},
  {id:'ct3',name:'陈晓',pinyin:'C',phone:'135 7789 2233',region:'广东省深圳市南山区',remark:'高意向客户',avatar:'blue'},
  {id:'ct4',name:'何丽',pinyin:'H',phone:'159 3344 1122',region:'广东省深圳市南山区',remark:'',avatar:'orange'},
  {id:'ct5',name:'李芳',pinyin:'L',phone:'139 8832 0099',region:'广东省深圳市南山区',remark:'南山门店客户',avatar:'blue'},
  {id:'ct6',name:'李四',pinyin:'L',phone:'138 5521 3344',region:'广东省深圳市南山区',remark:'南山门店店员',avatar:'green'},
  {id:'ct7',name:'刘洋',pinyin:'L',phone:'158 3321 4455',region:'广东省深圳市宝安区',remark:'',avatar:'red'},
  {id:'ct8',name:'马超',pinyin:'M',phone:'188 5566 7788',region:'广东省深圳市福田区',remark:'福田门店客户',avatar:'blue'},
  {id:'ct9',name:'钱六',pinyin:'Q',phone:'137 4456 8899',region:'广东省深圳市福田区',remark:'福田门店店员',avatar:'green'},
  {id:'ct10',name:'孙婷婷',pinyin:'S',phone:'133 9900 1122',region:'广东省深圳市南山区',remark:'',avatar:'blue'},
  {id:'ct11',name:'王店长',pinyin:'W',phone:'136 2210 3344',region:'广东省深圳市南山区',remark:'南山门店店长',avatar:'blue'},
  {id:'ct12',name:'王建国',pinyin:'W',phone:'136 2210 5566',region:'广东省深圳市南山区',remark:'',avatar:'blue'},
  {id:'ct13',name:'王五',pinyin:'W',phone:'135 7789 9900',region:'广东省深圳市南山区',remark:'南山门店店员',avatar:'green'},
  {id:'ct14',name:'吴佳',pinyin:'W',phone:'186 1122 3344',region:'广东省深圳市南山区',remark:'',avatar:'blue'},
  {id:'ct15',name:'徐世敏',pinyin:'X',phone:'130 3325 8577',region:'广东省广州市天河区',remark:'',avatar:'blue'},
  {id:'ct16',name:'张三',pinyin:'Z',phone:'138 5521 6677',region:'广东省深圳市南山区',remark:'高意向客户',avatar:'blue'},
  {id:'ct17',name:'赵敏',pinyin:'Z',phone:'137 4456 5544',region:'广东省深圳市福田区',remark:'已成交客户',avatar:'blue'},
  {id:'ct18',name:'郑伟',pinyin:'Z',phone:'131 5544 6677',region:'广东省深圳市宝安区',remark:'',avatar:'blue'},
  {id:'ct19',name:'周磊',pinyin:'Z',phone:'150 6677 8899',region:'广东省深圳市宝安区',remark:'黑名单',avatar:'red'}
];

var FRIEND_REQUESTS = [
  {id:'fr1',name:'林小红',phone:'155 6677 8899',msg:'你好，我是林小红，想添加你为好友',time:'今天 10:30',status:'pending',avatar:'orange'},
  {id:'fr2',name:'黄志强',phone:'186 9900 1122',msg:'你好，我是宝安门店的黄志强',time:'昨天 15:20',status:'pending',avatar:'blue'},
  {id:'fr3',name:'周店长',phone:'136 2210 7788',msg:'你好，我是宝安门店店长',time:'昨天 09:00',status:'pending',avatar:'green'},
  {id:'fr4',name:'赵店长',phone:'137 4456 3344',msg:'',time:'3天前',status:'accepted',avatar:'blue'},
  {id:'fr5',name:'孙店员',phone:'158 3321 5566',msg:'你好',time:'5天前',status:'rejected',avatar:'green'}
];

var MESSAGE_LIST = [
  {id:'g2',name:'南山门店客户群',preview:'李四：张三客户已经到店了，正在介绍新品。',time:'13:22',badge:2,avatar:'blue',avatarText:'南'},
  {id:'g4',name:'五一直播专场群',preview:'主播李薇：王五的问题我已记录，运营同事跟进处理。',time:'12:00',badge:0,avatar:'orange',avatarText:'五'},
  {id:'ct6',name:'李四',preview:'好的，我马上跟进。',time:'11:30',badge:1,avatar:'green',avatarText:'李'},
  {id:'g3',name:'福田门店客户群',preview:'赵敏：希望新群主能尽快确定',time:'昨天',badge:0,avatar:'red',avatarText:'福'},
  {id:'g6',name:'瑜伽课程群',preview:'张磊：课程内容已更新',time:'昨天',badge:0,avatar:'purple',avatarText:'瑜'},
  {id:'ct11',name:'王店长',preview:'加油！有需要支持随时说。',time:'昨天',badge:0,avatar:'blue',avatarText:'王'},
  {id:'g1',name:'华南区代理群',preview:'华南区代理负责人：各门店注意查收通知。',time:'前天',badge:0,avatar:'blue',avatarText:'华'},
  {id:'g5',name:'618大促直播群',preview:'主播李薇：酒水租赁直播将于5月20日开播',time:'前天',badge:0,avatar:'orange',avatarText:'6'}
];

var currentContactSearch = '';

function renderMessageList() {
  var search = document.getElementById('globalSearch').value.toLowerCase();
  var filtered = MESSAGE_LIST.filter(function(m){
    if(search && m.name.indexOf(search)<0 && m.preview.indexOf(search)<0) return false;
    return true;
  });
  document.getElementById('msgListPage').innerHTML = filtered.map(function(m){
    var badgeHtml = m.badge > 0 ? '<div class="msg-item-badge">'+m.badge+'</div>' : '';
    var avBg = m.avatar==='blue'?'var(--primary)':m.avatar==='green'?'var(--success)':m.avatar==='orange'?'var(--warning)':m.avatar==='red'?'var(--danger)':'var(--purple)';
    return '<div class="msg-item" onclick="openMsgFromList(\''+m.id+'\')"><div class="msg-item-avatar" style="background:'+avBg+'">'+m.avatarText+'</div><div class="msg-item-content"><div class="msg-item-name">'+m.name+'</div><div class="msg-item-preview">'+m.preview+'</div></div><div class="msg-item-meta"><div class="msg-item-time">'+m.time+'</div>'+badgeHtml+'</div></div>';
  }).join('');
}

function openMsgFromList(id) {
  var g = GROUPS.find(function(x){return x.id===id});
  if(g) { openMsg(id); return; }
  showToast('打开对话');
}

function renderContactList() {
  var search = currentContactSearch.toLowerCase();
  var filtered = CONTACTS.filter(function(c){
    if(search && c.name.indexOf(search)<0 && c.pinyin.indexOf(search.toUpperCase())<0 && c.phone.indexOf(search)<0) return false;
    return true;
  });
  var grouped = {};
  filtered.forEach(function(c){
    var letter = c.pinyin.charAt(0).toUpperCase();
    if(!grouped[letter]) grouped[letter] = [];
    grouped[letter].push(c);
  });
  var letters = Object.keys(grouped).sort();
  var html = '';
  letters.forEach(function(letter){
    html += '<div class="contact-section"><div class="section-header" id="section-'+letter+'">'+letter+'</div>';
    grouped[letter].forEach(function(c){
      var avBg = c.avatar==='blue'?'var(--primary)':c.avatar==='green'?'var(--success)':c.avatar==='orange'?'var(--warning)':c.avatar==='red'?'var(--danger)':'var(--purple)';
      html += '<div class="contact-item" onclick="showFriendDetail(\''+c.id+'\')"><div class="contact-avatar" style="background:'+avBg+'">'+c.name.charAt(0)+'</div><span class="contact-name">'+c.name+'</span></div>';
    });
    html += '</div>';
  });
  if(letters.length === 0) html = '<div class="empty-state"><div class="empty-icon">🔍</div><div class="empty-text">未找到联系人</div></div>';
  document.getElementById('contactList').innerHTML = html;
  document.getElementById('alphaIndex').innerHTML = letters.map(function(l){return '<span onclick="scrollToSection(\''+l+'\')">'+l+'</span>';}).join('');
}

function scrollToSection(letter) {
  var el = document.getElementById('section-'+letter);
  if(el) el.scrollIntoView({behavior:'smooth',block:'start'});
}

function handleContactSearch(v) { currentContactSearch = v; renderContactList(); }
function toggleAddMenu() { document.getElementById('addMenu').classList.toggle('show'); }
function closeAddMenu() { document.getElementById('addMenu').classList.remove('show'); }

function updateNewFriendBadge() {
  var count = FRIEND_REQUESTS.filter(function(f){return f.status==='pending'}).length;
  var badge = document.getElementById('newFriendBadge');
  if(count > 0) { badge.style.display = 'inline'; badge.textContent = count; }
  else { badge.style.display = 'none'; }
}

function showNewFriends() {
  closeAddMenu();
  document.getElementById('subNavTitle').textContent = '新的朋友';
  document.getElementById('subNavAction').innerHTML = '';
  var html = '<div style="padding:0">';
  if(FRIEND_REQUESTS.length === 0) {
    html += '<div class="empty-state"><div class="empty-icon">📭</div><div class="empty-text">暂无新的朋友</div></div>';
  } else {
    FRIEND_REQUESTS.forEach(function(fr){
      var avBg = fr.avatar==='blue'?'var(--primary)':fr.avatar==='green'?'var(--success)':fr.avatar==='orange'?'var(--warning)':'var(--danger)';
      var statusHtml = '';
      if(fr.status === 'pending') statusHtml = '<button class="btn btn-wechat btn-sm" onclick="acceptFriend(\''+fr.id+'\')">通过</button>';
      else if(fr.status === 'accepted') statusHtml = '<span style="font-size:12px;color:var(--text-tertiary)">已添加</span>';
      else if(fr.status === 'rejected') statusHtml = '<span style="font-size:12px;color:var(--text-tertiary)">已拒绝</span>';
      html += '<div class="friend-request-item"><div class="friend-request-avatar" style="background:'+avBg+'">'+fr.name.charAt(0)+'</div><div class="friend-request-info"><div class="friend-request-name">'+fr.name+'</div><div class="friend-request-msg">'+(fr.msg||'请求添加你为朋友')+'</div></div>'+statusHtml+'</div>';
    });
  }
  html += '</div>';
  document.getElementById('subPageContent').innerHTML = html;
  document.getElementById('subPage').classList.add('show');
}

function acceptFriend(id) {
  var fr = FRIEND_REQUESTS.find(function(f){return f.id===id});
  if(fr) { fr.status = 'accepted'; showToast('已通过'+fr.name+'的好友申请'); showNewFriends(); updateNewFriendBadge(); }
}

function showAddFriend() {
  closeAddMenu();
  document.getElementById('subNavTitle').textContent = '添加好友';
  document.getElementById('subNavAction').innerHTML = '';
  document.getElementById('subPageContent').innerHTML = '<div style="padding:16px"><div style="display:flex;gap:8px;margin-bottom:16px"><input class="search-input" placeholder="请输入手机号" id="addFriendPhone" style="flex:1;padding:0 12px"><button class="btn btn-wechat" onclick="searchFriend()">搜索</button></div><div id="addFriendResult"></div></div>';
  document.getElementById('subPage').classList.add('show');
}

function searchFriend() {
  var phone = document.getElementById('addFriendPhone').value.trim();
  var result = document.getElementById('addFriendResult');
  if(!phone) { result.innerHTML = '<div class="empty-state"><div class="empty-icon">🔍</div><div class="empty-text">请输入手机号</div></div>'; return; }
  var found = CONTACTS.find(function(c){return c.phone.replace(/\s/g,'').indexOf(phone.replace(/\s/g,''))>=0});
  if(found) {
    var avBg = found.avatar==='blue'?'var(--primary)':found.avatar==='green'?'var(--success)':found.avatar==='orange'?'var(--warning)':found.avatar==='red'?'var(--danger)':'var(--purple)';
    result.innerHTML = '<div style="background:var(--bg-card);border-radius:8px;padding:16px;display:flex;align-items:center;gap:12px"><div class="contact-avatar" style="background:'+avBg+';width:48px;height:48px;font-size:20px;border-radius:8px">'+found.name.charAt(0)+'</div><div style="flex:1"><div style="font-size:16px;font-weight:600">'+found.name+'</div><div style="font-size:13px;color:var(--text-secondary);margin-top:2px">'+found.region+'</div></div><button class="btn btn-wechat btn-sm" onclick="showApplyFriend(\''+found.id+'\')">添加</button></div>';
  } else {
    result.innerHTML = '<div class="empty-state"><div class="empty-icon">😔</div><div class="empty-text">该用户不存在</div></div>';
  }
}

function showApplyFriend(contactId) {
  var c = CONTACTS.find(function(x){return x.id===contactId});
  if(!c) return;
  document.getElementById('subNavTitle').textContent = '申请添加好友';
  var avBg = c.avatar==='blue'?'var(--primary)':c.avatar==='green'?'var(--success)':c.avatar==='orange'?'var(--warning)':c.avatar==='red'?'var(--danger)':'var(--purple)';
  document.getElementById('subPageContent').innerHTML = '<div style="padding:16px"><div style="background:var(--bg-card);border-radius:8px;padding:16px;display:flex;align-items:center;gap:12px;margin-bottom:16px"><div class="friend-avatar-lg" style="background:'+avBg+'">'+c.name.charAt(0)+'</div><div class="friend-basic"><div class="friend-name-lg">'+c.name+'</div><div class="friend-remark">'+c.region+'</div></div></div><div style="margin-bottom:16px"><div style="font-size:14px;color:var(--text-secondary);margin-bottom:8px">打招呼</div><textarea style="width:100%;height:80px;border:1px solid var(--border);border-radius:8px;padding:10px;font-size:14px;font-family:inherit;resize:none;outline:none" placeholder="我是...">你好，我是'+ROLES[currentRole].identity+'，想添加你为好友</textarea></div><button class="btn btn-wechat btn-block" onclick="showToast(\'好友申请已发送\');closeSubPage()">发送申请</button></div>';
}

function showFriendDetail(contactId) {
  var c = CONTACTS.find(function(x){return x.id===contactId});
  if(!c) return;
  document.getElementById('subNavTitle').textContent = '';
  document.getElementById('subNavAction').innerHTML = '<span style="cursor:pointer;font-size:18px" onclick="showFriendSettings(\''+c.id+'\')">⋯</span>';
  var avBg = c.avatar==='blue'?'var(--primary)':c.avatar==='green'?'var(--success)':c.avatar==='orange'?'var(--warning)':c.avatar==='red'?'var(--danger)':'var(--purple)';
  var remarkHtml = c.remark ? '<div class="friend-remark">昵称：'+c.name+'</div>' : '';
  var nameDisplay = c.remark || c.name;
  var groupsHtml = '';
  var customerData = CUSTOMERS.find(function(x){return x.name===c.name});
  if(customerData && customerData.groups.length > 0) {
    groupsHtml = customerData.groups.map(function(g){
      return '<div class="member-card" style="margin:0 0 8px"><div class="member-avatar '+(g.type==='直播群'?'orange':g.type==='课程群'?'purple':'blue')+'">群</div><div class="member-info"><div class="member-name">'+g.name+'</div><div class="member-meta">'+g.type+'｜群主：'+g.owner+'</div></div></div>';
    }).join('');
  } else {
    groupsHtml = '<div style="font-size:13px;color:var(--text-tertiary);padding:8px 0">暂无共同群聊</div>';
  }
  document.getElementById('subPageContent').innerHTML = '<div class="friend-info-card"><div class="friend-avatar-lg" style="background:'+avBg+'">'+c.name.charAt(0)+'</div><div class="friend-basic"><div class="friend-name-lg">'+nameDisplay+'</div>'+remarkHtml+'</div></div><div class="friend-detail-row"><span class="friend-detail-label">地区</span><span class="friend-detail-value">'+c.region+'</span></div><div class="friend-detail-row"><span class="friend-detail-label">电话</span><span class="friend-detail-value" style="color:var(--wechat-green)">'+c.phone+'</span></div><div class="friend-actions"><button class="action-btn primary" onclick="showToast(\'打开对话\')">发消息</button><button class="action-btn outline" onclick="showToast(\'语音/视频通话\')">语音/视频</button></div><div style="height:8px;background:var(--bg-page)"></div><div style="padding:16px"><div class="section-title" style="padding-left:0">关联群</div>'+groupsHtml+'</div>';
  document.getElementById('subPage').classList.add('show');
}

function showFriendSettings(contactId) {
  var c = CONTACTS.find(function(x){return x.id===contactId});
  if(!c) return;
  document.getElementById('subNavTitle').textContent = '朋友设置';
  document.getElementById('subNavAction').innerHTML = '';
  document.getElementById('subPageContent').innerHTML = '<div style="padding:0"><div class="friend-detail-row" onclick="showEditRemark(\''+c.id+'\')"><span class="friend-detail-label" style="flex:1">设置朋友名称</span><span style="color:var(--text-tertiary);font-size:14px">›</span></div><div class="friend-detail-row" onclick="showToast(\'已拉黑\')"><span class="friend-detail-label" style="flex:1;color:var(--danger)">拉黑好友</span></div><div class="friend-detail-row" onclick="confirmDeleteFriend(\''+c.id+'\')"><span class="friend-detail-label" style="flex:1;color:var(--danger)">删除好友</span></div></div>';
}

function showEditRemark(contactId) {
  var c = CONTACTS.find(function(x){return x.id===contactId});
  if(!c) return;
  document.getElementById('subNavTitle').textContent = '修改朋友备注名';
  document.getElementById('subPageContent').innerHTML = '<div style="padding:16px"><div style="margin-bottom:16px"><input type="text" style="width:100%;height:40px;border:1px solid var(--border);border-radius:8px;padding:0 12px;font-size:14px;font-family:inherit;outline:none" placeholder="请输入备注名" value="'+(c.remark||'')+'" id="remarkInput"></div><div style="display:flex;gap:12px"><button class="btn btn-outline" style="flex:1" onclick="showFriendSettings(\''+c.id+'\')">取消</button><button class="btn btn-wechat" style="flex:1" onclick="saveRemark(\''+c.id+'\')">确定</button></div></div>';
}

function saveRemark(contactId) {
  var c = CONTACTS.find(function(x){return x.id===contactId});
  if(!c) return;
  var input = document.getElementById('remarkInput');
  if(input) c.remark = input.value;
  showToast('备注名已保存');
  showFriendSettings(contactId);
}

function confirmDeleteFriend(contactId) {
  var c = CONTACTS.find(function(x){return x.id===contactId});
  if(!c) return;
  document.getElementById('confirmTitle').textContent = '提示';
  document.getElementById('confirmBody').innerHTML = '删除后将同时删除与<strong>'+c.name+'</strong>的聊天记录';
  document.getElementById('confirmOk').onclick = function(){ closeConfirm(); showToast('已删除好友'); closeSubPage(); };
  document.getElementById('confirmDialog').classList.add('show');
}

function closeConfirm() { document.getElementById('confirmDialog').classList.remove('show'); }

function showMyGroups() {
  closeAddMenu();
  document.getElementById('subNavTitle').textContent = '我的群聊';
  document.getElementById('subNavAction').innerHTML = '';
  var myGroups = GROUPS.filter(function(g){return isMyGroup(g)});
  var html = '<div style="padding:0">';
  myGroups.forEach(function(g){
    var statusCls = getStatusClass(g.status);
    var avBg = g.type==='直播群'?'var(--warning)':g.type==='课程群'?'var(--purple)':'var(--primary)';
    html += '<div class="msg-item" onclick="showGroupDetail(\''+g.id+'\')"><div class="msg-item-avatar" style="background:'+avBg+'">'+g.name.charAt(0)+'</div><div class="msg-item-content"><div class="msg-item-name">'+g.name+'</div><div class="msg-item-preview">'+g.type+'｜'+g.members+'人</div></div><div class="msg-item-meta"><span class="group-status '+statusCls+'" style="font-size:10px;padding:1px 6px">'+g.status+'</span></div></div>';
  });
  html += '</div>';
  document.getElementById('subPageContent').innerHTML = html;
  document.getElementById('subPage').classList.add('show');
}

function showCreateGroup() {
  closeAddMenu();
  document.getElementById('subNavTitle').textContent = '创建群聊';
  document.getElementById('subNavAction').innerHTML = '';
  var html = '<div style="padding:16px"><div style="margin-bottom:12px;font-size:14px;font-weight:600">选择成员</div>';
  CONTACTS.forEach(function(c){
    var avBg = c.avatar==='blue'?'var(--primary)':c.avatar==='green'?'var(--success)':c.avatar==='orange'?'var(--warning)':c.avatar==='red'?'var(--danger)':'var(--purple)';
    html += '<div class="contact-item" onclick="this.querySelector(\'input\').checked=!this.querySelector(\'input\').checked" style="cursor:pointer"><div class="contact-avatar" style="background:'+avBg+';width:36px;height:36px;font-size:14px">'+c.name.charAt(0)+'</div><span class="contact-name">'+c.name+'</span><input type="checkbox" style="margin-left:auto;width:18px;height:18px;accent-color:var(--wechat-green)"></div>';
  });
  html += '<div style="margin-top:16px"><button class="btn btn-wechat btn-block" onclick="showToast(\'群聊创建成功\');closeSubPage()">立即创建</button></div></div>';
  document.getElementById('subPageContent').innerHTML = html;
  document.getElementById('subPage').classList.add('show');
}

function showGroupChatDetail(groupId) {
  var g = GROUPS.find(function(x){return x.id===groupId});
  if(!g) return;
  document.getElementById('subNavTitle').textContent = '群详情';
  document.getElementById('subNavAction').innerHTML = '';
  document.getElementById('subPageContent').innerHTML = '<div style="padding:0"><div class="friend-info-card"><div style="flex:1"><div class="friend-name-lg">'+g.name+'</div><div class="friend-remark">'+g.type+'｜'+g.members+'人</div></div></div><div class="group-detail-section"><div class="group-detail-row" onclick="showGroupMembers(\''+g.id+'\')"><span class="group-detail-label">群成员</span><span class="group-detail-value">'+g.members+'人</span><span class="group-detail-arrow">›</span></div><div class="group-detail-row"><span class="group-detail-label">群公告</span><span class="group-detail-value">暂无</span><span class="group-detail-arrow">›</span></div><div class="group-detail-row"><span class="group-detail-label">群ID</span><span class="group-detail-value">'+g.id.toUpperCase()+'</span></div></div><div class="group-detail-section"><div class="group-detail-row" onclick="showToast(\'转让群组\')"><span class="group-detail-label">转让群组</span><span class="group-detail-arrow">›</span></div><div class="group-detail-row" onclick="showToast(\'退出群组\')" style="color:var(--danger)"><span class="group-detail-label" style="color:var(--danger)">退出群组</span><span class="group-detail-arrow">›</span></div></div></div>';
  document.getElementById('subPage').classList.add('show');
}

function showGroupMembers(groupId) {
  var g = GROUPS.find(function(x){return x.id===groupId});
  if(!g) return;
  document.getElementById('subNavTitle').textContent = '群成员';
  document.getElementById('subNavAction').innerHTML = '';
  var html = '<div class="search-bar"><input class="search-input" placeholder="搜索群成员"></div><div style="padding:0">';
  g.memberList.forEach(function(m){
    var avBg = m.avatar==='blue'?'var(--primary)':m.avatar==='green'?'var(--success)':m.avatar==='orange'?'var(--warning)':m.avatar==='red'?'var(--danger)':'var(--purple)';
    html += '<div class="contact-item"><div class="contact-avatar" style="background:'+avBg+'">'+m.name.charAt(0)+'</div><span class="contact-name">'+m.name+'</span><span style="font-size:12px;color:var(--text-tertiary)">'+m.role+'</span></div>';
  });
  html += '</div>';
  document.getElementById('subPageContent').innerHTML = html;
}

"""

content = content.replace(
    "/* ========== Init ========== */",
    new_js + "\n/* ========== Init ========== */",
    1
)

with open("/Users/elton/Desktop/AI主播稿+通讯录副本/移动端通讯录与群管理工作台原型.html", "w", encoding="utf-8") as f:
    f.write(content)

print("File restructured successfully!")
