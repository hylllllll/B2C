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
    goods.gclick += goods.gclick
    goods.save()

    news_adv = goods.gtype.goodsinfo_set.order_by('-id')[0:2]
    context = {'page': 0,
               'goods': goods,
               'news_adv': news_adv,
               'id': int(id)}
    # print(goods)
    return render(request, 'df_goods/detail.html', context)