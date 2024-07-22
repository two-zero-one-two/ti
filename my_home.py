'''我的主页'''
import streamlit as st
from PIL import Image
import time

page = st.sidebar.radio('我的首页', ['兴趣推荐', '我的图片处理工具', '智慧词典','网页推荐' ,'评价','留言区'])
"""
工作室名字：线上工作室li.
"""
"""
根据地用户：分享后所有人可见
"""
"""
根据地用途：数据收集、兴趣推荐、经历分享、综合主站……
"""
"""
最喜欢的现有模块：兴趣推荐、我的图片处理工具、智慧词典、留言区
"""
"""
现有模块改进灵感：
"""
"""
原创模块：
"""
"""
原创模块一句话功能介：
"""
def page_1():
    '''兴趣推荐'''
    st.image('aduan_天象奇景.jpg')
    st.write('深邃的星空是那么令人向往')
    st.image('星空.png')
    with open('wet hands.mp3','rb') as f:
        mymp3 = f.read()
    st.audio(mymp3,format='audio/mp3', start_time = 0)

def page_2():
    '''我的图片处理工具'''
    st.write(":sunglasses:图片换色小程序:sunglasses:")
    uploaded_file = st.file_uploader('上传图片',type=['png','jpg','png'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)

        tab1, tab2, tab3, tab4 = st.tabs(['原图', '改色1', '改色2', '改色3'])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img, 0, 2, 1))
        with tab3:
            st.image(img_change(img, 1, 2, 0))
        with tab4:
            st.image(img_change(img, 1, 0, 2))
 
def page_3():
    '''智慧词典'''
    with open('words_space.txt','r',encoding='utf-8') as f:
            words_list = f.read().split('\n')
    
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    
    words_dict = {}
    st.image('6.png')
    for w in words_list:
        words_dict[w[1]] = [int(w[0]),w[2]]

    with open('check_out_times.txt','r',encoding='utf-8') as f:
        times_list = f.read().split('\n')
    
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
        
    word = st.text_input('输入抽查询的单词：')
    if word in words_dict:
        st.write(f'### :blue[{words_dict[word][1]}]')
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1

        st.write('查询次数:',n)
    with open('check_out_times.txt','w',encoding='utf-8') as f:
        message = ''
        for k,v in times_dict.items():
            message += str(k) + '#' + str(v) + '\n'
        message = message[:-1]
        f.write(message)

def page_4():
    '''留言区'''
    st.write('我的留言区')
    with open('leave_messages.txt','r',encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')

    for i in messages_list:
        if i[1] == '阿短':
            with st.chat_message('☀️'):
                st.write(i[1]+': '+i[2])
        elif i[1] == '编程猫':
            with st.chat_message('🌈'):
                st.write(i[1]+': '+i[2])
    name = st.selectbox('我是......',['阿短','编程猫'])
    new_message = st.text_input('想要说的话...')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt','w',encoding='utf-8') as f:
            message= ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)

def page_5():
    st.link_button('百度首页', 'https://www.baidu.com/')
    st.link_button('抖音', 'https://www.douyin.com/')

def page_6():
    st.write('你对此网站的评价是？(满分30)')
    col1, col2 = st.columns([1,1])
    with col1:
        cb1 = st.checkbox('A.5')
    with col2:
        cb2 = st.checkbox('B.10')
    col3, col4 = st.columns([1,1])
    with col3:
        cb3 = st.checkbox('C.15')
    with col4:
        cb4 = st.checkbox('D.20')
    col5, col6 = st.columns([1,1])
    with col5:
        cb5 = st.checkbox('E.23')
    with col6:
        cb6 = st.checkbox('F.25')
    col7, col8 = st.columns([1,1])
    with col7:
        cb7 = st.checkbox('G.27')
    with col8:
        cb8 = st.checkbox('H.29')
        b1 = st.button('提交')
    if b1:
        if cb1 == True or cb2 == True or cb3 == True:
            st.write('好的，我会改进。')
        elif cb4 == True or cb5 == True:
            st.write('感谢支持，我会继续改进。')
        elif cb6 == True or cb7 == True or cb8 == True:
            st.write('谢谢赞同，我会继续努力。')

def img_change(img,rc,bc,gc):
    width,height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x, y][0]
            g = img_array[x, y][1]
            b = img_array[x, y][2]
            img_array[x, y] = (b, g, r)
    return img
    
if page == '兴趣推荐':
    roading = st.progress(0, '开始加载')
    for i in range(1, 101, 1):
        time.sleep(0.02)
        roading.progress(i, '正在加载'+str(i)+'%')
    roading.progress(100, '加载完毕！')
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '智慧词典':
    page_3()
elif page == '留言区':
    page_4()
elif page == '网页推荐':
    page_5()
elif page == '评价':
    page_6()

