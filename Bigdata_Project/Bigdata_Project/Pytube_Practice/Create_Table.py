import pymysql
# alter charset to 'utf8mb4' to insert imoji

conn = pymysql.connect(host='13.58.15.95', port= 3306, user='Habeen',password='jih4412',db='test')
 
cur = conn.cursor(pymysql.cursors.DictCursor)

sql = """
CREATE TABLE `youtube` (
	`vid_url` VARCHAR(500) NULL DEFAULT NULL COLLATE 'utf8mb4_unicode_ci',
	`title` VARCHAR(500) NULL DEFAULT NULL COLLATE 'utf8mb4_unicode_ci',
	`length` VARCHAR(1000) NULL DEFAULT NULL COLLATE 'utf8mb4_unicode_ci',
	`rating` VARCHAR(1000) NULL DEFAULT NULL COLLATE 'utf8mb4_unicode_ci',
	`thumbnail` VARCHAR(1000) NULL DEFAULT NULL COLLATE 'utf8mb4_unicode_ci',
	`views` VARCHAR(1000) NULL DEFAULT NULL COLLATE 'utf8mb4_unicode_ci',
	`description` VARCHAR(10000) NULL DEFAULT NULL COLLATE 'utf8mb4_unicode_ci',
	`crawl_time` TIMESTAMP NULL DEFAULT NULL
)
COLLATE='utf8mb4_unicode_ci'
ENGINE=InnoDB
;

"""

cur.execute(sql)
conn.commit()
print('table created')

conn.close()