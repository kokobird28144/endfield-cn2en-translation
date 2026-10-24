# 游戏物品与设施中英对照

共 309 条分版本名称记录；按 ItemTable 的 name.id 与同一版本 CN/EN 表配对。原有1.5.3记录保留，新增1.6.4补充见下方。

数据快照：`1.5.3@10024360-6`，另含 `1.6.4@11123848-6` 的166条分版本核验记录；核验日期：2026-10-19。`game-data-paired` 表示已核对社区镜像中的双语数据，**不表示已在当前游戏界面逐项复核**。

结构化主表为 [game-terms.csv](game-terms.csv)，包含物品 ID、名称文本 ID、版本、状态和条件性简称。来源与局限见 [sources.md](sources.md)。

筛选范围：175 份中文语料中的生产物料/设施，加上常见矿物、加工材料、药品、电池与物流设施。并非全游戏物品百科。排除仅因“协议”“掌握”等普通词碰巧命中的非生产物品；同名瓶装内容物和系统蓝图不重复列入。

英文保留数据表大小写、连字符与 [A]/[B]/[C] 等等级标记。简称只是候选，不可无条件替换。

## 物品与物料

| 中文规范名 | 英文名称 | 条件性简称 | 物品 ID |
| --- | --- | --- | --- |
| 实验息壤铜锭 | Proto Xiran-Cuprium |  | item_activity_copper_poly |
| 实验息壤铜零件 | Proto Xiran-Cuprium Part |  | item_activity_copper_poly_cmpt |
| 实验息壤铜气 | Proto Xiran-Cuprium Gas |  | item_activity_copper_poly_gas |
| 实验息壤铜骨骼 | Proto Xiran-Cuprium Frame |  | item_activity_copper_poly_tool |
| 实验铜骨骼 | Proto Cuprium Frame |  | item_activity_copper_xiranite_tool |
| 援助成果券 | Fruits of Altruism Certs |  | item_activity_relief_coupon |
| 实验龙泡泡外壳 | Proto Chubby Lung Shell |  | item_activity_xiranite_box |
| 实验龙泡泡重壳 | Proto Chubby Lung Heavy Shell |  | item_activity_xiranite_enr_box |
| 重息壤龙泡泡 | Heavy Xiranite Chubby Lung |  | item_activity_xiranite_enr_lung |
| 实验重息壤块 | Proto Heavy Xiranite |  | item_activity_xiranite_enr_nugget |
| 息壤葫芦 | Xiranite Gourd |  | item_activity_xiranite_hulu |
| 息壤龙泡泡 | Xiranite Chubby Lung |  | item_activity_xiranite_lung |
| 实验息壤块 | Proto Xiranite |  | item_activity_xiranite_nugget |
| 荞愈胶囊 | Buck Capsule [C] |  | item_bottled_rec_hp_1 |
| 优质荞愈胶囊 | Buck Capsule [B] |  | item_bottled_rec_hp_2 |
| 精选荞愈胶囊 | Buck Capsule [A] |  | item_bottled_rec_hp_3 |
| 芽针针剂 | Yazhen Syringe [C] | 蓝药（小药另查别名表） | item_bottled_rec_hp_4 |
| 优质芽针针剂 | Yazhen Syringe [A] |  | item_bottled_rec_hp_5 |
| 稳定碳块 | Stabilized Carbon |  | item_carbon_enr |
| 致密碳粉末 | Dense Carbon Powder |  | item_carbon_enr_powder |
| 碳块 | Carbon |  | item_carbon_mtl |
| 碳粉末 | Carbon Powder |  | item_carbon_powder |
| 赤铜瓶 | Cuprium Bottle |  | item_copper_bottle |
| 赤铜零件 | Cuprium Part |  | item_copper_cmpt |
| 赫铜块 | Hetonite |  | item_copper_enr |
| 灼铜块 | Pyrrolite |  | item_copper_enr2 |
| 灼铜零件 | Pyrrolite Part | 灼件 | item_copper_enr2_cmpt |
| 赫铜瓶 | Hetonite Bottle |  | item_copper_enr_bottle |
| 赫铜零件 | Hetonite Part | 赫件 | item_copper_enr_cmpt |
| 赤铜耐压罐 | Cuprium Canister |  | item_copper_jar |
| 赤铜块 | Cuprium |  | item_copper_nugget |
| 赤铜矿 | Cuprium Ore |  | item_copper_ore |
| 赤铜粉末 | Cuprium Powder |  | item_copper_powder |
| 密制晶体 | Packed Origocrust |  | item_crystal_enr |
| 致密晶体粉末 | Dense Origocrust Powder |  | item_crystal_enr_powder |
| 晶体外壳粉末 | Origocrust Powder |  | item_crystal_powder |
| 晶体外壳 | Origocrust |  | item_crystal_shell |
| 分离芯 | Separator Core |  | item_filter_core |
| 酸气 | Acridgen |  | item_gas_acid |
| 气态赤铜 | Cuprium Gas |  | item_gas_copper |
| 气态赫铜 | Hetonite Gas |  | item_gas_copper_enr |
| 气态灼铜 | Pyrrolite Gas |  | item_gas_copper_enr2 |
| 惰气 | Inergen |  | item_gas_inert |
| 息壤气 | Xiragen |  | item_gas_xiranite |
| 重息壤气 | Heavy Xiragen |  | item_gas_xiranite_enr |
| 紫晶零件 | Amethyst Part |  | item_glass_cmpt |
| 蓝铁瓶 | Ferrium Bottle |  | item_iron_bottle |
| 铁制零件 | Ferrium Part | 铁零件 | item_iron_cmpt |
| 蓝铁块 | Ferrium |  | item_iron_nugget |
| 蓝铁矿 | Ferrium Ore |  | item_iron_ore |
| 蓝铁粉末 | Ferrium Powder |  | item_iron_powder |
| 沉积酸 | Precipitation Acid |  | item_liquid_acid |
| 赤铜溶液 | Cuprium Solution |  | item_liquid_copper |
| 锦草溶液 | Jincao Solution |  | item_liquid_plant_grass_1 |
| 芽针溶液 | Yazhen Solution |  | item_liquid_plant_grass_2 |
| 污水 | Sewage |  | item_liquid_sewage |
| 清水 | Clean Water | 水 | item_liquid_water |
| 液化息壤 | Liquid Xiranite |  | item_liquid_xiranite |
| 惰性壤晶废液 | Inert Xircon Effluent |  | item_liquid_xiranite_lowpoly |
| 壤晶废液 | Xircon Effluent | 废液 | item_liquid_xiranite_poly |
| 致密源石粉末 | Dense Originium Powder |  | item_originium_enr_powder |
| 源矿 | Originium Ore |  | item_originium_ore |
| 源石粉末 | Originium Powder |  | item_originium_powder |
| 锦草 | Jincao |  | item_plant_grass_1 |
| 芽针 | Yazhen |  | item_plant_grass_2 |
| 锦草粉末 | Jincao Powder |  | item_plant_grass_powder_1 |
| 芽针粉末 | Yazhen Powder |  | item_plant_grass_powder_2 |
| 锦草种子 | Jincao Seed |  | item_plant_grass_seed_1 |
| 芽针种子 | Yazhen Seeds |  | item_plant_grass_seed_2 |
| 荞花 | Buckflower |  | item_plant_moss_1 |
| 砂叶 | Sandleaf |  | item_plant_moss_3 |
| 细磨荞花粉末 | Ground Buckflower Powder |  | item_plant_moss_enr_powder_1 |
| 荞花粉末 | Buckflower Powder |  | item_plant_moss_powder_1 |
| 砂叶粉末 | Sandleaf Powder |  | item_plant_moss_powder_3 |
| 砂叶种子 | Sandleaf Seed |  | item_plant_moss_seed_3 |
| 低容谷地电池 | LC Valley Battery |  | item_proc_battery_1 |
| 中容谷地电池 | SC Valley Battery |  | item_proc_battery_2 |
| 高容谷地电池 | HC Valley Battery |  | item_proc_battery_3 |
| 低容武陵电池 | LC Wuling Battery |  | item_proc_battery_4 |
| 中容武陵电池 | SC Wuling Battery | 中电;中融武陵电池 | item_proc_battery_5 |
| 紫晶纤维 | Amethyst Fiber |  | item_quartz_glass |
| 紫晶矿 | Amethyst Ore |  | item_quartz_sand |
| 重息壤 | Heavy Xiranite |  | item_xiranite_enr_powder |
| 壤晶 | Xircon |  | item_xiranite_poly |
| 息壤 | Xiranite |  | item_xiranite_powder |

## 设施与物流部件

| 中文规范名 | 英文名称 | 条件性简称 | 物品 ID |
| --- | --- | --- | --- |
| 传送带 | Transport Belt |  | item_log_belt_01 |
| 物品准入口 | Item Control Port | 准入口 | item_log_conditioner |
| 物流桥 | Belt Bridge |  | item_log_connector |
| 汇流器 | Converger |  | item_log_converger |
| 管道 | Pipe |  | item_log_pipe_01 |
| 管道准入口 | Pipe Control Port | 准入口 | item_log_pipe_conditioner |
| 管道桥 | Pipe Bridge |  | item_log_pipe_connector |
| 管道汇流器 | Pipe Converger |  | item_log_pipe_converger |
| 管道分流器 | Pipe Splitter |  | item_log_pipe_splitter |
| 分流器 | Splitter |  | item_log_splitter |
| 便捷存取站 | Easy Stash |  | item_port_carrier_1 |
| 配件机 | Fitting Unit |  | item_port_cmpt_mc_1 |
| 拆解机 | Separating Unit |  | item_port_dismantler_1 |
| 给水器 | Fluid Supply Unit |  | item_port_dumper_1 |
| 灌装机 | Filling Unit |  | item_port_filling_pd_mc_1 |
| 精炼炉 | Refining Unit |  | item_port_furnance_1 |
| 气体收集泵 | Gas Extractor |  | item_port_gas_pump_1 |
| 气体反应炉 | Gas Reactor Globe |  | item_port_gas_reactor_1 |
| 储气罐 | Gas Tank |  | item_port_gas_storager_1 |
| 粉碎机 | Shredding Unit |  | item_port_grinder_1 |
| 废水处理机 | Water Treatment Unit |  | item_port_liquid_cleaner_1 |
| 提纯机 | Purification Unit |  | item_port_liquid_purifier_1 |
| 储液罐 | Fluid Tank |  | item_port_liquid_storager_1 |
| 仓库存货口 | Depot Loader | 存货口;存入口 | item_port_loader_1 |
| 仓库存取线基段 | Depot Bus Section |  | item_port_log_hongs_bus |
| 仓库存取线源桩 | Depot Bus Port |  | item_port_log_hongs_bus_source |
| 便携源石矿机 | Portable Originium Rig |  | item_port_miner_1 |
| 电驱矿机 | Electric Mining Rig |  | item_port_miner_2 |
| 二型电驱矿机 | Electric Mining Rig Mk II |  | item_port_miner_3 |
| 水驱矿机 | Hydro Mining Rig |  | item_port_miner_4 |
| 反应池 | Reactor Crucible |  | item_port_mix_pool_1 |
| 扩容反应池 | Expanded Crucible |  | item_port_mix_pool_2 |
| 液气转化机 | Fluid-Gas Transmuting Unit | 液气机 | item_port_phase_trans_1 |
| 固气转化机 | Solid-Gas Transmuting Unit | 固气机 | item_port_phase_trans_2 |
| 种植机 | Planting Unit |  | item_port_planter_1 |
| 供电桩 | Electric Pylon |  | item_port_power_diffuser_1 |
| 息壤供电桩 | Xiranite Pylon |  | item_port_power_diffuser_2 |
| 中继器 | Relay Tower |  | item_port_power_pole_2 |
| 息壤中继器 | Xiranite Relay |  | item_port_power_pole_3 |
| 供电终端 | Electric Nexus |  | item_port_power_port_1 |
| 热能池 | Thermal Bank |  | item_port_power_sta_1 |
| 水泵 | Fluid Pump |  | item_port_pump_1 |
| 二型耐酸水泵 | Acid Resistant Pump Mk II |  | item_port_pump_2 |
| 采种机 | Seed-Picking Unit |  | item_port_seedcol_1 |
| 塑形机 | Moulding Unit |  | item_port_shaper_1 |
| 协议核心 | Protocol Automation-Core (PAC) |  | item_port_sp_hub_1 |
| 次级核心 | Sub-PAC |  | item_port_sp_sub_hub_1 |
| 协议储存箱 | Protocol Stash | 储存箱;存储箱;箱子 | item_port_storager_1 |
| 研磨机 | Grinding Unit |  | item_port_thickener_1 |
| 封装机 | Packaging Unit |  | item_port_tools_asm_mc_1 |
| 暗管入口 | Conduit Inlet |  | item_port_udpipe_loader_1 |
| 多口暗管入口 | Conduit Inlet Manifold |  | item_port_udpipe_loader_2 |
| 暗管出口 | Conduit Outlet |  | item_port_udpipe_unloader_1 |
| 多口暗管出口 | Conduit Outlet Manifold |  | item_port_udpipe_unloader_2 |
| 仓库取货口 | Depot Unloader | 取货口 | item_port_unloader_1 |
| 气体散布机 | Gas Dispersing Unit |  | item_port_vaporizer_1 |
| 装备原件机 | Gearing Unit |  | item_port_winder_1 |
| 天有洪炉 | Forge of the Sky | 洪炉;烘炉 | item_port_xiranite_oven_1 |

## 使用边界

所有简称的限制说明保存在 CSV 的 notes 字段及 [translation-guide.md](translation-guide.md)。例如“准入口”同时对应两种设备，“中电”需要地区，“废液”需要具体物料上下文。协议核心的物品名与建筑名存在差异，不静默覆盖。

## 1.6.4 补充核验

本节对应 `1.6.4@11123848-6`，用于本次新抓取中的菜品、食材、旅馆及相关物品；不覆盖历史版本条目。文本ID由Python整数精确读取。

| 中文规范名 | 英文名称 | 物品 ID |
| --- | --- | --- |
| 面粉 | Flour | item_Ingredient_flour_1 |
| 菜籽油 | Seed Oil | item_Ingredient_oil_1 |
| 辣椒粉 | Ground Pepper | item_Ingredient_paprika_1 |
| 一百三十香 | Spice Mix 130 | item_Ingredient_spices_1 |
| 淀粉 | Starch | item_Ingredient_starch_1 |
| 砂糖 | Sugar | item_Ingredient_sugar_1 |
| 球豆壳 | Ballpea Pod | item_byproduct_bean_1 |
| 球豆壳粉末 | Ballpea Pod Powder | item_byproduct_bean_moss_1 |
| 平薯叶 | Pingtuber Leaf | item_byproduct_potato_1 |
| 球豆 | Ballpea | item_corp_bean_1 |
| 青菜 | Cabbage | item_corp_cabbage_1 |
| 优质青菜 | Cabbage [A] | item_corp_cabbage_2 |
| 籽油花 | Oilseed Bloom | item_corp_canolaflower_1 |
| 多味菇 | Relishroom | item_corp_mushroom_1 |
| 优质多味菇 | Relishroom [A] | item_corp_mushroom_2 |
| 平薯 | Pingtuber | item_corp_potato_1 |
| 青叶莓 | Sourberry | item_corp_strawberry_1 |
| 优质青叶莓 | Sourberry [A] | item_corp_strawberry_2 |
| 脆蔗 | Crunchcane | item_corp_sugarcane_1 |
| 茄果 | Matoberry | item_corp_tomato_1 |
| 白瓜 | Whitemelon | item_corp_whitegourd_1 |
| 谷地调度券 | Valley Stock Bill | item_domain_tundra_coupon |
| 草籽干粉 | Powdered Grass Seed | item_drop_lbmob_1 |
| 息壤装备原件 | Xiranite Component | item_equip_script_4 |
| 水蒸气 | Aquagen | item_gas_water |
| 折金票 | T-Creds | item_gold |
| 肉包子 | Meat Baozi | item_inn_dish_1 |
| 糯米凉糕 | Sticky Rice Cake | item_inn_dish_10 |
| 鲜奶炖蛋 | Steamed Flan | item_inn_dish_11 |
| 豌杂拌面 | Pea-Topped Noodles | item_inn_dish_12 |
| 手抓饭 | Meaty Pilaf | item_inn_dish_13 |
| 鳞肉水饺 | Fin Dumpling | item_inn_dish_14 |
| 炸薯条 | Tuber Fries | item_inn_dish_15 |
| 酸菜鳞肉 | Fin & Pickled Greens | item_inn_dish_16 |
| 烤肉串 | Roasted Kebab | item_inn_dish_17 |
| 鳞香肉丝 | Fin-Savory Shreds | item_inn_dish_18 |
| 豆沙汤圆 | Beanpaste Tangyuan | item_inn_dish_19 |
| 手擀素面 | Hand-Kneaded Noodle | item_inn_dish_2 |
| 酸莓布丁 | Sourberry Pudding | item_inn_dish_20 |
| 咸酪脆饼 | Salted Cheese Crackers | item_inn_dish_21 |
| 雪绵豆沙 | Sweetbeans on Snow | item_inn_dish_22 |
| 老麻抄手 | Chaoshou & Numbing Sauce | item_inn_dish_23 |
| 八宝饭 | Eight Treasure Rice | item_inn_dish_24 |
| 至臻鳞肉卷 | Roll of Fin-Supreme | item_inn_dish_25 |
| 界龙肉卷 | Boundary Lung Roll | item_inn_dish_26 |
| 果味沙拉 | Berry Fruity Toss | item_inn_dish_27 |
| 麻辣香锅 | Mala Xiang Guo | item_inn_dish_28 |
| 坛子肉 | Clay Jar Meat | item_inn_dish_29 |
| 番茄炒蛋 | Mato & Egg | item_inn_dish_3 |
| 福寿全 | Immortal Galore of Fortune | item_inn_dish_30 |
| 糖醋宝鳞 | Sweet & Sour Fingot | item_inn_dish_31 |
| “银耳莲子”羹 | "Snowshroom & Lotus" Soup | item_inn_dish_32 |
| 茄果鳞肉汤 | Fin-Mato Soup | item_inn_dish_33 |
| 酸辣汤 | Hot & Sour Soup | item_inn_dish_34 |
| 白瓜肉丸汤 | Melon & Meatball Soup | item_inn_dish_35 |
| 奶油蘑菇汤 | Cream of Shroom | item_inn_dish_36 |
| 白鳞高汤 | White Fin Broth | item_inn_dish_37 |
| 莓果甜汤 | Berry-Sweet Sip | item_inn_dish_38 |
| 簇锦豆腐羹 | Tofu Bouquet Soup | item_inn_dish_39 |
| 红椒土豆丝 | Shredded Tuber & Pepper | item_inn_dish_4 |
| 金丝小贝 | Goldfloss Chiffon | item_inn_dish_40 |
| 雪纱蛋黄月饼 | Snow-Veiled Mooncake | item_inn_dish_41 |
| 千果珍珠圆 | Pearly Fruit Punch | item_inn_dish_42 |
| 红蕊奶酪蛋糕 | Redbloom Cheesecake | item_inn_dish_43 |
| “勺里游” | "Spoon Swimmer" | item_inn_dish_44 |
| 缘缘菜饭 | Yuanyuan Veggy Rice | item_inn_dish_5 |
| 菌菇蒸饺 | Shroom Dumpling | item_inn_dish_6 |
| 青菜养生粥 | Tonic Congee & Greens | item_inn_dish_7 |
| 香煎鳞肉 | Skilleted Fin | item_inn_dish_8 |
| 茄汁白瓜 | Melon in Sauce | item_inn_dish_9 |
| 大碗碎茶 | Bowl of Tea | item_inn_drink_1 |
| 瓶装霞莓饮 | Bottled Duskberry Juice | item_inn_drink_10 |
| 瓶装兽奶 | Bottled Milk | item_inn_drink_2 |
| 玉米汁 | Corn Juice | item_inn_drink_3 |
| 瓶装脆蔗汁 | Bottled Canejuice | item_inn_drink_4 |
| 梨花香茶 | Pear Blossom Tea | item_inn_drink_5 |
| 游人酒 | Seeker's Kohl | item_inn_drink_6 |
| 瓶装优质兽奶 | Bottled Milk [A] | item_inn_drink_7 |
| 陈酿葡萄露 | Vintage Grapedew | item_inn_drink_8 |
| 潮前龙井 | Pre-Tide Lungjing | item_inn_drink_9 |
| 直饮水 | Potable Water | item_inn_drink_water |
| 肉包子食谱 | Recipe: Meat Baozi | item_inn_recipe_1 |
| 糯米凉糕食谱 | Recipe: Sticky Rice Cake | item_inn_recipe_10 |
| 鲜奶炖蛋食谱 | Recipe: Steamed Flan | item_inn_recipe_11 |
| 豌杂拌面食谱 | Recipe: Pea-Topped Noodles | item_inn_recipe_12 |
| 手抓饭食谱 | Recipe: Meaty Pilaf | item_inn_recipe_13 |
| 鳞肉水饺食谱 | Recipe: Fin Dumpling | item_inn_recipe_14 |
| 炸薯条食谱 | Recipe: Tuber Fries | item_inn_recipe_15 |
| 酸菜鳞肉食谱 | Recipe: Fin & Pickled Greens | item_inn_recipe_16 |
| 烤肉串食谱 | Recipe: Roasted Kebab | item_inn_recipe_17 |
| 鳞香肉丝食谱 | Recipe: Fin-Savory Shreds | item_inn_recipe_18 |
| 豆沙汤圆食谱 | Recipe: Beanpaste Tangyuan | item_inn_recipe_19 |
| 手擀素面食谱 | Recipe: Hand-Kneaded Noodle | item_inn_recipe_2 |
| 酸莓布丁食谱 | Recipe: Sourberry Pudding | item_inn_recipe_20 |
| 咸酪脆饼食谱 | Recipe: Salted Cheese Crackers | item_inn_recipe_21 |
| 雪绵豆沙食谱 | Recipe: Sweetbeans on Snow | item_inn_recipe_22 |
| 老麻抄手食谱 | Recipe: Chaoshou & Numbing Sauce | item_inn_recipe_23 |
| 八宝饭食谱 | Recipe: Eight Treasure Rice | item_inn_recipe_24 |
| 至臻鳞肉卷食谱 | Recipe: Roll of Fin-Supreme | item_inn_recipe_25 |
| 界龙肉卷食谱 | Recipe: Boundary Lung Roll | item_inn_recipe_26 |
| 果味沙拉食谱 | Recipe: Berry Fruity Toss | item_inn_recipe_27 |
| 麻辣香锅食谱 | Recipe: Mala Xiang Guo | item_inn_recipe_28 |
| 坛子肉食谱 | Recipe: Clay Jar Meat | item_inn_recipe_29 |
| 番茄炒蛋食谱 | Recipe: Mato & Egg | item_inn_recipe_3 |
| 福寿全食谱 | Recipe: Immortal Galore of Fortune | item_inn_recipe_30 |
| 糖醋宝鳞食谱 | Recipe: Sweet & Sour Fingot | item_inn_recipe_31 |
| “银耳莲子”羹食谱 | Recipe: "Snowshroom & Lotus" Soup | item_inn_recipe_32 |
| 茄果鳞肉汤食谱 | Recipe: Fin-Mato Soup | item_inn_recipe_33 |
| 酸辣汤食谱 | Recipe: Hot & Sour Soup | item_inn_recipe_34 |
| 白瓜肉丸汤食谱 | Recipe: Melon & Meatball Soup | item_inn_recipe_35 |
| 奶油蘑菇汤食谱 | Recipe: Cream of Shroom | item_inn_recipe_36 |
| 白鳞高汤食谱 | Recipe: White Fin Broth | item_inn_recipe_37 |
| 莓果甜汤食谱 | Recipe: Berry-Sweet Sip | item_inn_recipe_38 |
| 簇锦豆腐羹食谱 | Recipe: Tofu Bouquet Soup | item_inn_recipe_39 |
| 红椒土豆丝食谱 | Recipe: Shredded Tuber & Pepper | item_inn_recipe_4 |
| 金丝小贝食谱 | Recipe: Goldfloss Chiffon | item_inn_recipe_40 |
| 雪纱蛋黄月饼食谱 | Recipe: Snow-Veiled Mooncake | item_inn_recipe_41 |
| 千果珍珠圆食谱 | Recipe: Pearly Fruit Punch | item_inn_recipe_42 |
| 红蕊奶酪蛋糕食谱 | Recipe: Redbloom Cheesecake | item_inn_recipe_43 |
| “勺里游”食谱 | Recipe: "Spoon Swimmer" | item_inn_recipe_44 |
| 缘缘菜饭食谱 | Recipe: Yuanyuan Veggy Rice | item_inn_recipe_5 |
| 菌菇蒸饺食谱 | Recipe: Shroom Dumpling | item_inn_recipe_6 |
| 青菜养生粥食谱 | Recipe: Tonic Congee & Greens | item_inn_recipe_7 |
| 香煎鳞肉食谱 | Recipe: Skilleted Fin | item_inn_recipe_8 |
| 茄汁白瓜食谱 | Recipe: Melon in Sauce | item_inn_recipe_9 |
| 柑实 | Citrome | item_plant_moss_2 |
| 灰芦麦 | Reed Rye | item_plant_sp_1 |
| 苦叶椒 | Tartpepper | item_plant_sp_2 |
| 琼叶参 | Redjade Ginseng | item_plant_sp_3 |
| 金石稻 | Amber Rice | item_plant_sp_4 |
| 原木 | Wood | item_plant_tundra_wood |
| 洒水机 | Sprinkler | item_port_squirter_1 |
| 禽蛋 | Egg | item_ranch_egg_1 |
| 优质禽蛋 | Egg [A] | item_ranch_egg_2 |
| 鳞肉 | Fin Fillet | item_ranch_fishmeat_1 |
| 优质鳞肉 | Fin Fillet [A] | item_ranch_fishmeat_2 |
| 饱食饲料 | Yummy Feed | item_ranch_fodder_1 |
| 双效饱食饲料 | Double-Yummy Feed | item_ranch_fodder_2 |
| 肉块 | Meat | item_ranch_meat_1 |
| 优质肉块 | Meat [A] | item_ranch_meat_2 |
| 兽奶 | Milk | item_ranch_milk_1 |
| 优质兽奶 | Milk [A] | item_ranch_milk_2 |
| 小蜜虫布丁 | Mini Honey Slugpudding | item_slimeml_1_agrange_1_moss_2_1 |

## 1.6.4 玩家别名核验对应物品补充

用户别名另外管理；下列仍是按物品ID配对的规范名称。数据版本`1.6.4@11123848-6`。

| 中文规范名 | 英文名称 | 物品 ID |
| --- | --- | --- |
| 息壤玉葫芦 | Xiranite Jade Gourd | item_activity_xiranite_enr_hulu |
| 优质锦草软饮 | Jincao Tea | item_bottled_food_5 |
| 优质芽针针剂 | Yazhen Syringe [A] | item_bottled_rec_hp_5 |
| 赤铜块 | Cuprium | item_copper_nugget |
| 赤铜矿 | Cuprium Ore | item_copper_ore |
| 岳研避瘴茶货组 | Eureka Anti-smog Tincture [pkg] | item_domainshop_cargo_jinlong_2 |
| 浸雾大弩 | Haze-Soaked Ballista | item_drop_hvybow_1 |
| 紫晶质瓶 | Amethyst Bottle | item_glass_bottle |
| 高晶质瓶 | Cryston Bottle | item_glass_enr_bottle |
| 烟火钱 | Spirit Money | item_inn_gold |
| 钢制零件 | Steel Part | item_iron_enr_cmpt |
| 高容谷地电池 | HC Valley Battery | item_proc_battery_3 |

## 1.6.4用户补充核验

普通药品与副产物粉末按同版本精确ID配对。简称另见community-aliases，不把叶/壳与粉末合并。

| 中文规范名 | 英文名称 | 物品 ID |
| --- | --- | --- |
| 芽针针剂 | Yazhen Syringe [C] | item_bottled_rec_hp_4 |
| 锦草软饮 | Jincao Drink | item_bottled_food_4 |
| 平薯叶粉末 | Pingtuber Leaf Powder | item_byproduct_potato_moss_1 |

## 1.6.4审校奖励名核验

| 中文规范名 | 英文名称 | 物品 ID |
| --- | --- | --- |
| 嵌晶玉 | Oroberyl | item_diamond |
| 武器检查套组 | Arms INSP Set | item_weapon_expcard_high |
| 协议棱柱组 | Protohedron | item_char_skill_level_7_12 |
| 协议圆盘组 | Protoset | item_char_break_stage_3_4 |
| 高级认知载体 | Advanced Cognitive Carrier | item_expcard_stage2_high |
| 高阶培养自选箱Ⅰ | Advanced Progression Selection Crate Ⅰ | item_case_bp_selfselect_skillsp_1 |
| 泡泡出击 | Chubby Lung Attacks | item_user_avatar_activity_9 |
| 存续的痕迹 | Mark of Perseverance | item_char_skill_crown |
