from django.shortcuts import render
from .models import TypeInfo, GoodsInfo
from django.core.paginator import Paginator


def index(request):
    # 查询各分类最新或最热的数据
    typelist = TypeInfo.objects.all()
    type0 = typelist[0].goodsinfo_set.order_by('-id')[0:4]
    type01 = typelist[0].goodsinfo_set.order_by('-gclick')[0:4]
    type1 = typelist[1].goodsinfo_set.order_by('-id')[0:4]
    type11 = typelist[1].goodsinfo_set.order_by('-gclick')[0:4]
    # type2 = typelist[2].goodsinfo_set.order_by('-id')[0:4]
    # type21 = typelist[2].goodsinfo_set.order_by('-gclick')[0:4]
    # type3 = typelist[3].goodsinfo_set.order_by('-id')[0:4]
    # type31 = typelist[3].goodsinfo_set.order_by('-gclick')[0:4]
    # type4 = typelist[4].goodsinfo_set.order_by('-id')[0:4]
    # type41 = typelist[4].goodsinfo_set.order_by('-gclick')[0:4]
    # type5 = typelist[5].goodsinfo_set.order_by('-id')[0:4]
    # type51 = typelist[5].goodsinfo_set.order_by('-gclick')[0:4]

    context = {'page': 0,  # page是为了对应base_foot_top_search模板中的搜索框和购物车样式的判断
               'typelist': typelist,
               'type0': type0, 'type01': type01,
               'type1': type1, 'type11': type11}
               # 'type2': type2, 'type21': type21,
               # 'type3': type3, 'type31': type31,
               # 'type4': type4, 'type41': type41,
               # 'type5': type5, 'type51': type51,
               # }
    # print(typelist)
    return render(request, 'df_goods/index.html', context)


def list(request, tid, page_index, sort):  # tid对应商品类， page_index对应页码， sort对应排序的规则
    """一个商品类的所有商品"""

    typeinfo = TypeInfo.objects.get(pk=int(tid))
    news_adv = typeinfo.goodsinfo_set.order_by('-id')[0:2]

    if sort=='1':  # 默认，用‘最新’规则排序
        goods_list = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-id')  # 注意字段gtype_id字段是外键
    elif sort=='2':
        goods_list = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-gprice')  # 价格排
    elif sort=='3':
        goods_list = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-gclick')  # 人气排

    # print(goods_list)
    # print(typeinfo)
    # 对商品进行分页
    paginator = Paginator(goods_list, 10)
    page = paginator.page(int(page_index))
    # list1 = range(20)
    # print(list1)

    context = {'page': 1,
               'npage': page,
               'paginator': paginator,
               'typeinfo': typeinfo,
               'sort': sort,
               'news_adv': news_adv}
               # 'list': list1}

    return render(request, 'df_goods/list.html', context)


def detail(request, id):
    """一个商品的详细介绍页"""

    goods = GoodsInfo.objects.get(pk=id)
    goods.gclick += 1
    goods.save()

    news_adv = goods.gtype.goodsinfo_set.order_by('-id')[0:2]
    context = {'page': 0,
               'goods': goods,
               'news_adv': news_adv,
               'id': int(id)}
    # print(goods)
    response = render(request, 'df_goods/detail.html', context)

    # 在详情页设置用户最近浏览记录，用商品id来记录（到cookies）
    # 先获取cookies中的记录，默认值为空字符串
    goods_ids = request.COOKIES.get('goods_ids', '')
    goods_id = '%d'%goods.id
    if goods_ids != '':  # 判断浏览记录是否为空（新用户没浏览过商品）
        goods_ids_list = goods_ids.split(',')  # 用逗号将字符串分割（因为存储格式为含逗号的字符串'1, 2, 3'）返回列表['1', '2', '3']
        if goods_id in goods_ids_list:
            # print(goods_id, goods_ids_list)
            goods_ids_list.remove(goods_id)  # 如果已存在，删除，后面再加入（以保持最新）
        goods_ids_list.append(goods_id)  # 在加到最后
        if len(goods_ids_list)>5:
            del goods_ids_list[5]  # 多与5个则删除第六个
        goods_ids = ','.join(goods_ids_list)  # 用','将每个元素拼接为字符串
    else:  # 为空，直接记录
        goods_ids = goods_id
    response.set_cookie('goods_ids', goods_ids)  # 将更新后的数据写入cookies

    return response

