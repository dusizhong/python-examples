/*
MySQL Data Transfer
Source Host: localhost
Source Database: ador
Target Host: localhost
Target Database: ador
Date: 2016/8/17 15:54:08
*/

SET FOREIGN_KEY_CHECKS=0;
-- ----------------------------
-- Table structure for product
-- ----------------------------
DROP TABLE IF EXISTS `product`;
CREATE TABLE `product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `desc` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `content` text COLLATE utf8_unicode_ci,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records 
-- ----------------------------
INSERT INTO `product` VALUES ('1', '水桶广告', '公司纯净水桶广告招商中', '公司纯净水桶广告是培森传媒2016年推出新型广告主题,现招商中,覆盖全市各大区域,低价效果极佳!', '2016-04-20 15:54:14');
INSERT INTO `product` VALUES ('2', '车体广告', '车体车贴广告火热招募中', '车体车贴广告火热招募中', '2016-04-26 10:58:20');
INSERT INTO `product` VALUES ('3', '人体广告', '你就是你,你就是广告', '你就是你,你就是广告,人体广告招募中', '2016-04-27 10:24:24');
