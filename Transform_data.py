import Read_source_data as rsd

def transf():
    gfh= rsd.read_src('products')
    gfh.drop_duplicates()
    cate = gfh['category']
    sd = cate.drop_duplicates()

    return sd

