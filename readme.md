# python进程间通信
- 导入模块
    两个不同的 Python 文件可以通过共享队列来进行通信。队列是一种先进先出（FIFO）的数据结构，可以在多个线程或进程之间安全地传递数据。
    在`controler.py`和`modeler.py`返回的时间如下
    ```
    [controler] Produced: Item 0 [time]1711613605.7526226
    [controler] Produced: Item 1 [time]1711613606.764137
    [controler] Produced: Item 2 [time]1711613607.77119
    [controler] Produced: Item 3 [time]1711613608.7811198
    [controler] Produced: Item 4 [time]1711613609.7917702
    [controler] Produced: Item 5 [time]1711613610.799743
    [controler] Produced: Item 6 [time]1711613611.8025124
    [controler] Produced: Item 7 [time]1711613612.8073974
    [controler] Produced: Item 8 [time]1711613613.8144746
    [controler] Produced: Item 9 [time]1711613614.8251128
    [controler] Produced: Item 10 [time]1711613615.8274739
    [controler] Produced: Item 11 [time]1711613616.837728
    [controler] Produced: Item 12 [time]1711613617.8448074
    [controler] Produced: Item 13 [time]1711613618.8537636
    [controler] Produced: Item 14 [time]1711613619.8597784
    [controler] Produced: Item 15 [time]1711613620.866785
    [controler] Produced: Item 16 [time]1711613621.8720286
    [controler] Produced: Item 17 [time]1711613622.8759704
    [controler] Produced: Item 18 [time]1711613623.886447
    [controler] Produced: Item 19 [time]1711613624.8950653
    [modeler]: Item 0 [time]1711613624.8960757
    [modeler]: Item 1 [time]1711613624.8960757
    [modeler]: Item 2 [time]1711613624.8970654
    [modeler]: Item 3 [time]1711613624.8970654
    [modeler]: Item 4 [time]1711613624.8970654
    [modeler]: Item 5 [time]1711613624.8980622
    [modeler]: Item 6 [time]1711613624.8980622
    [modeler]: Item 7 [time]1711613624.8980622
    [modeler]: Item 8 [time]1711613624.8980622
    [modeler]: Item 9 [time]1711613624.8990638
    [modeler]: Item 10 [time]1711613624.8990638
    [modeler]: Item 11 [time]1711613624.8990638
    [modeler]: Item 12 [time]1711613624.8990638
    [modeler]: Item 13 [time]1711613624.8990638
    [modeler]: Item 14 [time]1711613624.8990638
    [modeler]: Item 15 [time]1711613624.9000635
    [modeler]: Item 16 [time]1711613624.9000635
    [modeler]: Item 17 [time]1711613624.9000635
    [modeler]: Item 18 [time]1711613624.9000635
    [modeler]: Item 19 [time]1711613624.9000635
    ```
- 命令行参数
    不考虑
- 文件读写
    目前已经遇到的是，读写的时候发生堵塞
    在`controler_txt.py`和`modeler_txt.py`返回的时间如下
    ```
    > python .\modeler_txt.py
    cur lien 你好当前时间戳Thu Mar 28 16:23:20 2024
    cur lien 你好当前时间戳Thu Mar 28 16:23:21 2024
    cur lien 你好当前时间戳Thu Mar 28 16:23:22 2024
    cur lien 你好当前时间戳Thu Mar 28 16:23:23 2024
    cur lien 你好当前时间戳Thu Mar 28 16:23:24 2024
    cur lien 你好当前时间戳Thu Mar 28 16:23:25 2024
    cur lien 你好当前时间戳Thu Mar 28 16:23:26 2024
    cur lien 你好当前时间戳Thu Mar 28 16:23:27 2024
    cur lien 你好当前时间戳Thu Mar 28 16:23:28 2024
    cur lien 你好当前时间戳Thu Mar 28 16:23:29 2024
    ```