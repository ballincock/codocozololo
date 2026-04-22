CREATE TABLE `api_weather_logs` (
  `id` int(11) NOT NULL,
  `location` varchar(255) DEFAULT NULL,
  `temp` float DEFAULT NULL,
  `pressure` float DEFAULT NULL,
  `precip` float DEFAULT NULL,
  `wind_speed` float DEFAULT NULL,
  `wind_dir` varchar(10) DEFAULT NULL,
  `logged_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `trends` varchar(255) DEFAULT 'Stable'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `api_weather_logs` (`id`, `location`, `temp`, `pressure`, `precip`, `wind_speed`, `wind_dir`, `logged_at`, `trends`) VALUES
(1, 'Chicago', 47.2, 1019, 0, 9, 'N', '2026-04-10 06:29:47', 'Stable'),
(2, 'Chicago', 46.5, 1009.1, 0.018, 31, NULL, '2026-03-22 05:00:00', 'Stable'),
(3, 'Chicago', 34.6, 1029, 0, 21.7, NULL, '2026-03-23 05:00:00', 'Cold Front'),
(4, 'Chicago', 39.7, 1028, 0, 13.7, NULL, '2026-03-24 05:00:00', 'Stable'),
(5, 'Chicago', 46.5, 1009.1, 0.018, 31, NULL, '2026-03-22 05:00:00', 'Stable'),
(6, 'Chicago', 34.6, 1029, 0, 21.7, NULL, '2026-03-23 05:00:00', 'Cold Front'),
(7, 'Chicago', 39.7, 1028, 0, 13.7, NULL, '2026-03-24 05:00:00', 'Stable'),
(8, 'Chicago', 56.6, 1015.5, 0, 21.7, NULL, '2026-03-25 05:00:00', 'Stable'),
(9, 'Chicago', 46.5, 1009.1, 0.018, 31, NULL, '2026-03-22 05:00:00', 'Stable'),
(10, 'Chicago', 34.6, 1029, 0, 21.7, NULL, '2026-03-23 05:00:00', 'Cold Front'),
(11, 'Chicago', 39.7, 1028, 0, 13.7, NULL, '2026-03-24 05:00:00', 'Stable'),
(12, 'Chicago', 56.6, 1015.5, 0, 21.7, NULL, '2026-03-25 05:00:00', 'Stable'),
(13, 'Chicago', 45.5, 1019, 0, 9.2, 'NE', '2026-04-10 06:54:54', 'Stable'),
(14, 'Chicago', 45.5, 1020, NULL, NULL, NULL, '2026-04-10 07:08:58', 'Prob: 50% (TOUGH)'),
(15, 'Chicago', 45.5, 1020, NULL, NULL, NULL, '2026-04-10 07:09:36', 'Prob: 50% (TOUGH)'),
(16, 'Chicago', 45.5, 1020, NULL, NULL, NULL, '2026-04-10 07:09:36', 'Prob: 50% (TOUGH)'),
(17, 'Chicago', 45.5, 1020, NULL, NULL, NULL, '2026-04-10 07:10:12', 'Prob: 50% (TOUGH)'),
(18, 'Chicago', 46.3, 1020, NULL, NULL, NULL, '2026-04-10 08:32:25', 'Prob: 50% (TOUGH)'),
(19, 'Chicago', 46.3, 1019, 0.059, 5.8, 'NE', '2026-04-10 08:36:55', 'Stable'),
(20, 'Chicago', 46.3, 1019, 0.059, 5.8, 'NE', '2026-04-10 08:37:30', 'Stable'),
(21, 'Chicago', 46.3, 1019, 0.059, 5.8, 'NE', '2026-04-10 08:38:16', 'Stable'),
(22, 'Chicago', 44.5, 1018, NULL, NULL, NULL, '2026-04-10 09:39:31', 'Prob: 50% (TOUGH)'),
(23, 'Chicago', 42.1, 1029, 0, 3.5, 'NE', '2026-04-11 02:20:25', 'Stable'),
(24, 'Chicago', 42.1, 1029, 0, 3.5, 'NE', '2026-04-11 02:20:29', 'Stable'),
(25, 'Chicago', 42.1, 1029, 0, 3.5, 'NE', '2026-04-11 02:23:56', 'Stable'),
(26, 'Chicago', 42.1, 1029, 0, 3.5, 'NE', '2026-04-11 02:23:57', 'Stable'),
(27, 'Chicago', 42.1, 1029, 0, 3.5, 'NE', '2026-04-11 02:23:58', 'Stable'),
(28, 'Chicago', 42.1, 1029, 0, 3.5, 'NE', '2026-04-11 02:23:59', 'Stable'),
(29, 'Chicago', 42.1, 1029, 0, 3.5, 'NE', '2026-04-11 02:24:00', 'Stable'),
(30, 'Chicago', 42.1, 1029, 0, 3.5, 'NE', '2026-04-11 02:24:01', 'Stable'),
(31, 'Chicago', 46.5, 1009.1, 0.018, 31, NULL, '2026-03-22 05:00:00', 'Stable'),
(32, 'Chicago', 34.6, 1029, 0, 21.7, NULL, '2026-03-23 05:00:00', 'Cold Front'),
(33, 'Chicago', 39.7, 1028, 0, 13.7, NULL, '2026-03-24 05:00:00', 'Stable'),
(34, 'Chicago', 56.6, 1015.5, 0, 21.7, NULL, '2026-03-25 05:00:00', 'Stable'),
(35, 'Chicago', 54.1, 1009.3, 0.339, 29, NULL, '2026-03-26 05:00:00', 'Stable'),
(36, 'Chicago', 46.5, 1009.1, 0.018, 31, NULL, '2026-03-22 05:00:00', 'Stable'),
(37, 'Chicago', 34.6, 1029, 0, 21.7, NULL, '2026-03-23 05:00:00', 'Cold Front'),
(38, 'Chicago', 39.7, 1028, 0, 13.7, NULL, '2026-03-24 05:00:00', 'Stable'),
(39, 'Chicago', 56.6, 1015.5, 0, 21.7, NULL, '2026-03-25 05:00:00', 'Stable'),
(40, 'Chicago', 54.1, 1009.3, 0.339, 29, NULL, '2026-03-26 05:00:00', 'Stable'),
(41, 'Chicago', 46.5, 1009.1, 0.018, 31, NULL, '2026-03-22 05:00:00', 'Stable'),
(42, 'Chicago', 34.6, 1029, 0, 21.7, NULL, '2026-03-23 05:00:00', 'Cold Front'),
(43, 'Chicago', 39.7, 1028, 0, 13.7, NULL, '2026-03-24 05:00:00', 'Stable'),
(44, 'Chicago', 56.6, 1015.5, 0, 21.7, NULL, '2026-03-25 05:00:00', 'Stable'),
(45, 'Chicago', 54.1, 1009.3, 0.339, 29, NULL, '2026-03-26 05:00:00', 'Stable'),
(46, 'Chicago', 46.5, 1009.1, 0.018, 31, NULL, '2026-03-22 05:00:00', 'Stable'),
(47, 'Chicago', 34.6, 1029, 0, 21.7, NULL, '2026-03-23 05:00:00', 'Cold Front'),
(48, 'Chicago', 39.7, 1028, 0, 13.7, NULL, '2026-03-24 05:00:00', 'Stable'),
(49, 'Chicago', 56.6, 1015.5, 0, 21.7, NULL, '2026-03-25 05:00:00', 'Stable'),
(50, 'Chicago', 54.1, 1009.3, 0.339, 29, NULL, '2026-03-26 05:00:00', 'Stable'),
(51, 'Chicago', 46.5, 1009.1, 0.018, 31, NULL, '2026-03-22 05:00:00', 'Stable'),
(52, 'Chicago', 34.6, 1029, 0, 21.7, NULL, '2026-03-23 05:00:00', 'Cold Front'),
(53, 'Chicago', 39.7, 1028, 0, 13.7, NULL, '2026-03-24 05:00:00', 'Stable'),
(54, 'Chicago', 56.6, 1015.5, 0, 21.7, NULL, '2026-03-25 05:00:00', 'Stable'),
(55, 'Chicago', 54.1, 1009.3, 0.339, 29, NULL, '2026-03-26 05:00:00', 'Stable'),
(56, 'Chicago', 46.5, 1009.1, 0.018, 31, NULL, '2026-03-22 05:00:00', 'Stable'),
(57, 'Chicago', 34.6, 1029, 0, 21.7, NULL, '2026-03-23 05:00:00', 'Cold Front'),
(58, 'Chicago', 39.7, 1028, 0, 13.7, NULL, '2026-03-24 05:00:00', 'Stable'),
(59, 'Chicago', 56.6, 1015.5, 0, 21.7, NULL, '2026-03-25 05:00:00', 'Stable'),
(60, 'Chicago', 54.1, 1009.3, 0.339, 29, NULL, '2026-03-26 05:00:00', 'Stable'),
(61, 'Chicago', 46.5, 1009.1, 0.018, 31, NULL, '2026-03-22 05:00:00', 'Stable'),
(62, 'Chicago', 34.6, 1029, 0, 21.7, NULL, '2026-03-23 05:00:00', 'Cold Front'),
(63, 'Chicago', 39.7, 1028, 0, 13.7, NULL, '2026-03-24 05:00:00', 'Stable'),
(64, 'Chicago', 56.6, 1015.5, 0, 21.7, NULL, '2026-03-25 05:00:00', 'Stable'),
(65, 'Chicago', 54.1, 1009.3, 0.339, 29, NULL, '2026-03-26 05:00:00', 'Stable'),
(66, 'Chicago', 46.5, 1009.1, 0.018, 31, NULL, '2026-03-22 05:00:00', 'Stable'),
(67, 'Chicago', 34.6, 1029, 0, 21.7, NULL, '2026-03-23 05:00:00', 'Cold Front'),
(68, 'Chicago', 39.7, 1028, 0, 13.7, NULL, '2026-03-24 05:00:00', 'Stable'),
(69, 'Chicago', 56.6, 1015.5, 0, 21.7, NULL, '2026-03-25 05:00:00', 'Stable'),
(70, 'Chicago', 54.1, 1009.3, 0.339, 29, NULL, '2026-03-26 05:00:00', 'Stable'),
(71, 'Chicago', 46.5, 1009.1, 0.018, 31, NULL, '2026-03-22 05:00:00', 'Stable'),
(72, 'Chicago', 34.6, 1029, 0, 21.7, NULL, '2026-03-23 05:00:00', 'Cold Front'),
(73, 'Chicago', 39.7, 1028, 0, 13.7, NULL, '2026-03-24 05:00:00', 'Stable'),
(74, 'Chicago', 56.6, 1015.5, 0, 21.7, NULL, '2026-03-25 05:00:00', 'Stable'),
(75, 'Chicago', 54.1, 1009.3, 0.339, 29, NULL, '2026-03-26 05:00:00', 'Stable'),
(76, 'Chicago', 46.5, 1009.1, 0.018, 31, NULL, '2026-03-22 05:00:00', 'Stable'),
(77, 'Chicago', 34.6, 1029, 0, 21.7, NULL, '2026-03-23 05:00:00', 'Cold Front'),
(78, 'Chicago', 39.7, 1028, 0, 13.7, NULL, '2026-03-24 05:00:00', 'Stable'),
(79, 'Chicago', 56.6, 1015.5, 0, 21.7, NULL, '2026-03-25 05:00:00', 'Stable'),
(80, 'Chicago', 54.1, 1009.3, 0.339, 29, NULL, '2026-03-26 05:00:00', 'Stable'),
(81, 'Chicago', 46.5, 1009.1, 0.018, 31, NULL, '2026-03-22 05:00:00', 'Stable'),
(82, 'Chicago', 34.6, 1029, 0, 21.7, NULL, '2026-03-23 05:00:00', 'Cold Front'),
(83, 'Chicago', 39.7, 1028, 0, 13.7, NULL, '2026-03-24 05:00:00', 'Stable'),
(84, 'Chicago', 56.6, 1015.5, 0, 21.7, NULL, '2026-03-25 05:00:00', 'Stable'),
(85, 'Chicago', 54.1, 1009.3, 0.339, 29, NULL, '2026-03-26 05:00:00', 'Stable'),
(86, 'Chicago', 46.5, 1009.1, 0.018, 31, NULL, '2026-03-22 05:00:00', 'Stable'),
(87, 'Chicago', 34.6, 1029, 0, 21.7, NULL, '2026-03-23 05:00:00', 'Cold Front'),
(88, 'Chicago', 39.7, 1028, 0, 13.7, NULL, '2026-03-24 05:00:00', 'Stable'),
(89, 'Chicago', 56.6, 1015.5, 0, 21.7, NULL, '2026-03-25 05:00:00', 'Stable'),
(90, 'Chicago', 54.1, 1009.3, 0.339, 29, NULL, '2026-03-26 05:00:00', 'Stable'),
(91, 'Chicago', 46.5, 1009.1, 0.018, 31, NULL, '2026-03-22 05:00:00', 'Stable'),
(92, 'Chicago', 34.6, 1029, 0, 21.7, NULL, '2026-03-23 05:00:00', 'Cold Front'),
(93, 'Chicago', 39.7, 1028, 0, 13.7, NULL, '2026-03-24 05:00:00', 'Stable'),
(94, 'Chicago', 56.6, 1015.5, 0, 21.7, NULL, '2026-03-25 05:00:00', 'Stable'),
(95, 'Chicago', 54.1, 1009.3, 0.339, 29, NULL, '2026-03-26 05:00:00', 'Stable'),
(96, 'Chicago', 46.5, 1009.1, 0.018, 31, NULL, '2026-03-22 05:00:00', 'Stable'),
(97, 'Chicago', 34.6, 1029, 0, 21.7, NULL, '2026-03-23 05:00:00', 'Cold Front'),
(98, 'Chicago', 39.7, 1028, 0, 13.7, NULL, '2026-03-24 05:00:00', 'Stable'),
(99, 'Chicago', 56.6, 1015.5, 0, 21.7, NULL, '2026-03-25 05:00:00', 'Stable'),
(100, 'Chicago', 54.1, 1009.3, 0.339, 29, NULL, '2026-03-26 05:00:00', 'Stable'),
(101, 'Chicago', 46.5, 1009.1, 0.018, 31, NULL, '2026-03-22 05:00:00', 'Stable'),
(102, 'Chicago', 34.6, 1029, 0, 21.7, NULL, '2026-03-23 05:00:00', 'Cold Front'),
(103, 'Chicago', 39.7, 1028, 0, 13.7, NULL, '2026-03-24 05:00:00', 'Stable'),
(104, 'Chicago', 56.6, 1015.5, 0, 21.7, NULL, '2026-03-25 05:00:00', 'Stable'),
(105, 'Chicago', 54.1, 1009.3, 0.339, 29, NULL, '2026-03-26 05:00:00', 'Stable'),
(106, 'Chicago', 46.5, 1009.1, 0.018, 31, NULL, '2026-03-22 05:00:00', 'Stable'),
(107, 'Chicago', 34.6, 1029, 0, 21.7, NULL, '2026-03-23 05:00:00', 'Cold Front'),
(108, 'Chicago', 39.7, 1028, 0, 13.7, NULL, '2026-03-24 05:00:00', 'Stable'),
(109, 'Chicago', 56.6, 1015.5, 0, 21.7, NULL, '2026-03-25 05:00:00', 'Stable'),
(110, 'Chicago', 54.1, 1009.3, 0.339, 29, NULL, '2026-03-26 05:00:00', 'Stable'),
(111, 'Chicago', 46.5, 1009.1, 0.018, 31, NULL, '2026-03-22 05:00:00', 'Stable'),
(112, 'Chicago', 34.6, 1029, 0, 21.7, NULL, '2026-03-23 05:00:00', 'Cold Front'),
(113, 'Chicago', 39.7, 1028, 0, 13.7, NULL, '2026-03-24 05:00:00', 'Stable'),
(114, 'Chicago', 56.6, 1015.5, 0, 21.7, NULL, '2026-03-25 05:00:00', 'Stable'),
(115, 'Chicago', 54.1, 1009.3, 0.339, 29, NULL, '2026-03-26 05:00:00', 'Stable'),
(116, 'Chicago', 46.5, 1009.1, 0.018, 31, NULL, '2026-03-22 05:00:00', 'Stable'),
(117, 'Chicago', 34.6, 1029, 0, 21.7, NULL, '2026-03-23 05:00:00', 'Cold Front'),
(118, 'Chicago', 39.7, 1028, 0, 13.7, NULL, '2026-03-24 05:00:00', 'Stable'),
(119, 'Chicago', 56.6, 1015.5, 0, 21.7, NULL, '2026-03-25 05:00:00', 'Stable'),
(120, 'Chicago', 54.1, 1009.3, 0.339, 29, NULL, '2026-03-26 05:00:00', 'Stable'),
(121, 'Chicago', 46.5, 1009.1, 0.018, 31, NULL, '2026-03-22 05:00:00', 'Stable'),
(122, 'Chicago', 34.6, 1029, 0, 21.7, NULL, '2026-03-23 05:00:00', 'Cold Front'),
(123, 'Chicago', 39.7, 1028, 0, 13.7, NULL, '2026-03-24 05:00:00', 'Stable'),
(124, 'Chicago', 56.6, 1015.5, 0, 21.7, NULL, '2026-03-25 05:00:00', 'Stable'),
(125, 'Chicago', 54.1, 1009.3, 0.339, 29, NULL, '2026-03-26 05:00:00', 'Stable'),
(126, 'Chicago', 46.5, 1009.1, 0.018, 31, NULL, '2026-03-22 05:00:00', 'Stable'),
(127, 'Chicago', 34.6, 1029, 0, 21.7, NULL, '2026-03-23 05:00:00', 'Cold Front'),
(128, 'Chicago', 39.7, 1028, 0, 13.7, NULL, '2026-03-24 05:00:00', 'Stable'),
(129, 'Chicago', 56.6, 1015.5, 0, 21.7, NULL, '2026-03-25 05:00:00', 'Stable'),
(130, 'Chicago', 54.1, 1009.3, 0.339, 29, NULL, '2026-03-26 05:00:00', 'Stable'),
(131, 'Chicago', 46.5, 1009.1, 0.018, 31, NULL, '2026-03-22 05:00:00', 'Stable'),
(132, 'Chicago', 34.6, 1029, 0, 21.7, NULL, '2026-03-23 05:00:00', 'Cold Front'),
(133, 'Chicago', 39.7, 1028, 0, 13.7, NULL, '2026-03-24 05:00:00', 'Stable'),
(134, 'Chicago', 56.6, 1015.5, 0, 21.7, NULL, '2026-03-25 05:00:00', 'Stable'),
(135, 'Chicago', 54.1, 1009.3, 0.339, 29, NULL, '2026-03-26 05:00:00', 'Stable'),
(136, 'Chicago', 46.5, 1009.1, 0.018, 31, NULL, '2026-03-22 05:00:00', 'Stable'),
(137, 'Chicago', 34.6, 1029, 0, 21.7, NULL, '2026-03-23 05:00:00', 'Cold Front'),
(138, 'Chicago', 39.7, 1028, 0, 13.7, NULL, '2026-03-24 05:00:00', 'Stable'),
(139, 'Chicago', 56.6, 1015.5, 0, 21.7, NULL, '2026-03-25 05:00:00', 'Stable'),
(140, 'Chicago', 54.1, 1009.3, 0.339, 29, NULL, '2026-03-26 05:00:00', 'Stable'),
(141, 'Chicago', 46.5, 1009.1, 0.018, 31, NULL, '2026-03-22 05:00:00', 'Stable'),
(142, 'Chicago', 34.6, 1029, 0, 21.7, NULL, '2026-03-23 05:00:00', 'Cold Front'),
(143, 'Chicago', 39.7, 1028, 0, 13.7, NULL, '2026-03-24 05:00:00', 'Stable'),
(144, 'Chicago', 56.6, 1015.5, 0, 21.7, NULL, '2026-03-25 05:00:00', 'Stable'),
(145, 'Chicago', 54.1, 1009.3, 0.339, 29, NULL, '2026-03-26 05:00:00', 'Stable'),
(146, 'Chicago', 46.5, 1009.1, 0.018, 31, NULL, '2026-03-22 05:00:00', 'Stable'),
(147, 'Chicago', 34.6, 1029, 0, 21.7, NULL, '2026-03-23 05:00:00', 'Cold Front'),
(148, 'Chicago', 39.7, 1028, 0, 13.7, NULL, '2026-03-24 05:00:00', 'Stable'),
(149, 'Chicago', 56.6, 1015.5, 0, 21.7, NULL, '2026-03-25 05:00:00', 'Stable'),
(150, 'Chicago', 54.1, 1009.3, 0.339, 29, NULL, '2026-03-26 05:00:00', 'Stable'),
(151, 'Chicago', 46.5, 1009.1, 0.018, 31, NULL, '2026-03-22 05:00:00', 'Stable'),
(152, 'Chicago', 34.6, 1029, 0, 21.7, NULL, '2026-03-23 05:00:00', 'Cold Front'),
(153, 'Chicago', 39.7, 1028, 0, 13.7, NULL, '2026-03-24 05:00:00', 'Stable'),
(154, 'Chicago', 56.6, 1015.5, 0, 21.7, NULL, '2026-03-25 05:00:00', 'Stable'),
(155, 'Chicago', 54.1, 1009.3, 0.339, 29, NULL, '2026-03-26 05:00:00', 'Stable'),
(156, 'Chicago', 46.5, 1009.1, 0.018, 31, NULL, '2026-03-22 05:00:00', 'Stable'),
(157, 'Chicago', 34.6, 1029, 0, 21.7, NULL, '2026-03-23 05:00:00', 'Cold Front'),
(158, 'Chicago', 39.7, 1028, 0, 13.7, NULL, '2026-03-24 05:00:00', 'Stable'),
(159, 'Chicago', 56.6, 1015.5, 0, 21.7, NULL, '2026-03-25 05:00:00', 'Stable'),
(160, 'Chicago', 54.1, 1009.3, 0.339, 29, NULL, '2026-03-26 05:00:00', 'Stable'),
(161, 'Chicago', 46.5, 1009.1, 0.018, 31, NULL, '2026-03-22 05:00:00', 'Stable'),
(162, 'Chicago', 34.6, 1029, 0, 21.7, NULL, '2026-03-23 05:00:00', 'Cold Front'),
(163, 'Chicago', 39.7, 1028, 0, 13.7, NULL, '2026-03-24 05:00:00', 'Stable'),
(164, 'Chicago', 56.6, 1015.5, 0, 21.7, NULL, '2026-03-25 05:00:00', 'Stable'),
(165, 'Chicago', 54.1, 1009.3, 0.339, 29, NULL, '2026-03-26 05:00:00', 'Stable'),
(166, 'Chicago', 46.5, 1009.1, 0.018, 31, NULL, '2026-03-22 05:00:00', 'Stable'),
(167, 'Chicago', 34.6, 1029, 0, 21.7, NULL, '2026-03-23 05:00:00', 'Cold Front'),
(168, 'Chicago', 39.7, 1028, 0, 13.7, NULL, '2026-03-24 05:00:00', 'Stable'),
(169, 'Chicago', 56.6, 1015.5, 0, 21.7, NULL, '2026-03-25 05:00:00', 'Stable'),
(170, 'Chicago', 54.1, 1009.3, 0.339, 29, NULL, '2026-03-26 05:00:00', 'Stable'),
(171, 'Chicago', 46.5, 1009.1, 0.018, 31, NULL, '2026-03-22 05:00:00', 'Stable'),
(172, 'Chicago', 34.6, 1029, 0, 21.7, NULL, '2026-03-23 05:00:00', 'Cold Front'),
(173, 'Chicago', 39.7, 1028, 0, 13.7, NULL, '2026-03-24 05:00:00', 'Stable'),
(174, 'Chicago', 56.6, 1015.5, 0, 21.7, NULL, '2026-03-25 05:00:00', 'Stable'),
(175, 'Chicago', 54.1, 1009.3, 0.339, 29, NULL, '2026-03-26 05:00:00', 'Stable'),
(176, 'Chicago', 46.5, 1009.1, 0.018, 31, NULL, '2026-03-22 05:00:00', 'Stable'),
(177, 'Chicago', 34.6, 1029, 0, 21.7, NULL, '2026-03-23 05:00:00', 'Cold Front'),
(178, 'Chicago', 39.7, 1028, 0, 13.7, NULL, '2026-03-24 05:00:00', 'Stable'),
(179, 'Chicago', 56.6, 1015.5, 0, 21.7, NULL, '2026-03-25 05:00:00', 'Stable'),
(180, 'Chicago', 54.1, 1009.3, 0.339, 29, NULL, '2026-03-26 05:00:00', 'Stable'),
(181, 'Chicago', 46.5, 1009.1, 0.018, 31, NULL, '2026-03-22 05:00:00', 'Stable'),
(182, 'Chicago', 34.6, 1029, 0, 21.7, NULL, '2026-03-23 05:00:00', 'Cold Front'),
(183, 'Chicago', 39.7, 1028, 0, 13.7, NULL, '2026-03-24 05:00:00', 'Stable'),
(184, 'Chicago', 56.6, 1015.5, 0, 21.7, NULL, '2026-03-25 05:00:00', 'Stable'),
(185, 'Chicago', 54.1, 1009.3, 0.339, 29, NULL, '2026-03-26 05:00:00', 'Stable'),
(186, 'Chicago', 46.5, 1009.1, 0.018, 31, NULL, '2026-03-22 05:00:00', 'Stable'),
(187, 'Chicago', 34.6, 1029, 0, 21.7, NULL, '2026-03-23 05:00:00', 'Cold Front'),
(188, 'Chicago', 39.7, 1028, 0, 13.7, NULL, '2026-03-24 05:00:00', 'Stable'),
(189, 'Chicago', 56.6, 1015.5, 0, 21.7, NULL, '2026-03-25 05:00:00', 'Stable'),
(190, 'Chicago', 54.1, 1009.3, 0.339, 29, NULL, '2026-03-26 05:00:00', 'Stable'),
(191, 'Chicago', 46.5, 1009.1, 0.018, 31, NULL, '2026-03-22 05:00:00', 'Stable'),
(192, 'Chicago', 34.6, 1029, 0, 21.7, NULL, '2026-03-23 05:00:00', 'Cold Front'),
(193, 'Chicago', 39.7, 1028, 0, 13.7, NULL, '2026-03-24 05:00:00', 'Stable'),
(194, 'Chicago', 56.6, 1015.5, 0, 21.7, NULL, '2026-03-25 05:00:00', 'Stable'),
(195, 'Chicago', 54.1, 1009.3, 0.339, 29, NULL, '2026-03-26 05:00:00', 'Stable'),
(196, 'Chicago', 46.5, 1009.1, 0.018, 31, NULL, '2026-03-22 05:00:00', 'Stable'),
(197, 'Chicago', 34.6, 1029, 0, 21.7, NULL, '2026-03-23 05:00:00', 'Cold Front'),
(198, 'Chicago', 39.7, 1028, 0, 13.7, NULL, '2026-03-24 05:00:00', 'Stable'),
(199, 'Chicago', 56.6, 1015.5, 0, 21.7, NULL, '2026-03-25 05:00:00', 'Stable'),
(200, 'Chicago', 54.1, 1009.3, 0.339, 29, NULL, '2026-03-26 05:00:00', 'Stable'),
(201, 'Chicago', 46.5, 1009.1, 0.018, 31, NULL, '2026-03-22 05:00:00', 'Stable'),
(202, 'Chicago', 34.6, 1029, 0, 21.7, NULL, '2026-03-23 05:00:00', 'Cold Front'),
(203, 'Chicago', 39.7, 1028, 0, 13.7, NULL, '2026-03-24 05:00:00', 'Stable'),
(204, 'Chicago', 56.6, 1015.5, 0, 21.7, NULL, '2026-03-25 05:00:00', 'Stable'),
(205, 'Chicago', 54.1, 1009.3, 0.339, 29, NULL, '2026-03-26 05:00:00', 'Stable'),
(206, 'Chicago', 46.5, 1009.1, 0.018, 31, NULL, '2026-03-22 05:00:00', 'Stable'),
(207, 'Chicago', 34.6, 1029, 0, 21.7, NULL, '2026-03-23 05:00:00', 'Cold Front'),
(208, 'Chicago', 39.7, 1028, 0, 13.7, NULL, '2026-03-24 05:00:00', 'Stable'),
(209, 'Chicago', 56.6, 1015.5, 0, 21.7, NULL, '2026-03-25 05:00:00', 'Stable'),
(210, 'Chicago', 54.1, 1009.3, 0.339, 29, NULL, '2026-03-26 05:00:00', 'Stable'),
(211, 'Chicago', 46.5, 1009.1, 0.018, 31, NULL, '2026-03-22 05:00:00', 'Stable'),
(212, 'Chicago', 34.6, 1029, 0, 21.7, NULL, '2026-03-23 05:00:00', 'Cold Front'),
(213, 'Chicago', 39.7, 1028, 0, 13.7, NULL, '2026-03-24 05:00:00', 'Stable'),
(214, 'Chicago', 56.6, 1015.5, 0, 21.7, NULL, '2026-03-25 05:00:00', 'Stable'),
(215, 'Chicago', 54.1, 1009.3, 0.339, 29, NULL, '2026-03-26 05:00:00', 'Stable'),
(216, 'Chicago', 46.5, 1009.1, 0.018, 31, NULL, '2026-03-22 05:00:00', 'Stable'),
(217, 'Chicago', 46.5, 1009.1, 0.018, 31, NULL, '2026-03-22 05:00:00', 'Stable'),
(218, 'Chicago', 34.6, 1029, 0, 21.7, NULL, '2026-03-23 05:00:00', 'Cold Front'),
(219, 'Chicago', 34.6, 1029, 0, 21.7, NULL, '2026-03-23 05:00:00', 'Cold Front'),
(220, 'Chicago', 39.7, 1028, 0, 13.7, NULL, '2026-03-24 05:00:00', 'Stable'),
(221, 'Chicago', 39.7, 1028, 0, 13.7, NULL, '2026-03-24 05:00:00', 'Stable'),
(222, 'Chicago', 56.6, 1015.5, 0, 21.7, NULL, '2026-03-25 05:00:00', 'Stable'),
(223, 'Chicago', 56.6, 1015.5, 0, 21.7, NULL, '2026-03-25 05:00:00', 'Stable'),
(224, 'Chicago', 54.1, 1009.3, 0.339, 29, NULL, '2026-03-26 05:00:00', 'Stable'),
(225, 'Chicago', 54.1, 1009.3, 0.339, 29, NULL, '2026-03-26 05:00:00', 'Stable'),
(226, 'Chicago', 46.5, 1009.1, 0.018, 31, NULL, '2026-03-22 05:00:00', 'Stable'),
(227, 'Chicago', 34.6, 1029, 0, 21.7, NULL, '2026-03-23 05:00:00', 'Cold Front'),
(228, 'Chicago', 39.7, 1028, 0, 13.7, NULL, '2026-03-24 05:00:00', 'Stable'),
(229, 'Chicago', 56.6, 1015.5, 0, 21.7, NULL, '2026-03-25 05:00:00', 'Stable'),
(230, 'Chicago', 54.1, 1009.3, 0.339, 29, NULL, '2026-03-26 05:00:00', 'Stable'),
(231, 'Chicago', 46.5, 1009.1, 0.018, 31, NULL, '2026-03-22 05:00:00', 'Stable'),
(232, 'Chicago', 34.6, 1029, 0, 21.7, NULL, '2026-03-23 05:00:00', 'Cold Front'),
(233, 'Chicago', 39.7, 1028, 0, 13.7, NULL, '2026-03-24 05:00:00', 'Stable'),
(234, 'Chicago', 56.6, 1015.5, 0, 21.7, NULL, '2026-03-25 05:00:00', 'Stable'),
(235, 'Chicago', 54.1, 1009.3, 0.339, 29, NULL, '2026-03-26 05:00:00', 'Stable'),
(236, 'Chicago', 42.1, 1029, 0, 3.5, 'NE', '2026-04-11 02:26:39', 'Stable'),
(237, 'Chicago', 42.1, 1029, 0, 3.5, 'NE', '2026-04-11 02:26:40', 'Stable'),
(238, 'Chicago', 42.1, 1029, 0, 3.5, 'NE', '2026-04-11 02:26:44', 'Stable'),
(239, 'Chicago', 42.1, 1029, 0, 3.5, 'NE', '2026-04-11 02:26:44', 'Stable'),
(240, 'Chicago', 42.1, 1029, 0, 3.5, 'NE', '2026-04-11 02:26:45', 'Stable'),
(241, 'Chicago', 42.1, 1029, 0, 3.5, 'NE', '2026-04-11 02:26:45', 'Stable'),
(242, 'Chicago', 42.1, 1029, 0, 3.5, 'NE', '2026-04-11 02:28:29', 'Stable'),
(243, 'Chicago', 42.1, 1029, 0, 3.5, 'NE', '2026-04-11 02:28:29', 'Stable'),
(244, 'Chicago', 42.1, 1029, 0, 3.5, 'NE', '2026-04-11 02:28:29', 'Stable'),
(245, 'Chicago', 42.1, 1029, 0, 3.5, 'NE', '2026-04-11 02:28:30', 'Stable'),
(246, 'Chicago', 46.5, 1009.1, 0.018, 31, NULL, '2026-03-22 05:00:00', 'Stable'),
(247, 'Chicago', 34.6, 1029, 0, 21.7, NULL, '2026-03-23 05:00:00', 'Cold Front'),
(248, 'Chicago', 39.7, 1028, 0, 13.7, NULL, '2026-03-24 05:00:00', 'Stable'),
(249, 'Chicago', 56.6, 1015.5, 0, 21.7, NULL, '2026-03-25 05:00:00', 'Stable'),
(250, 'Chicago', 42.1, 1029, 0, 3.5, 'NE', '2026-04-11 02:31:58', 'Stable'),
(251, 'Chicago', 42.1, 1029, 0, 3.5, 'NE', '2026-04-11 02:31:58', 'Stable'),
(252, 'Chicago', 42.1, 1029, 0, 3.5, 'NE', '2026-04-11 02:31:59', 'Stable'),
(253, 'Chicago', 42.1, 1029, 0, 4, 'NE', '2026-04-11 02:37:45', 'Stable'),
(254, 'Chicago', 42.1, 1029, 0, 4, 'NE', '2026-04-11 02:41:55', 'Stable'),
(255, 'Chicago', 46.5, 1009.1, 0.018, 31, NULL, '2026-03-22 05:00:00', 'Stable'),
(256, 'Chicago', 34.6, 1029, 0, 21.7, NULL, '2026-03-23 05:00:00', 'Cold Front'),
(257, 'Chicago', 39.7, 1028, 0, 13.7, NULL, '2026-03-24 05:00:00', 'Stable'),
(258, 'Chicago', 42.1, 1029, NULL, NULL, NULL, '2026-04-11 02:42:17', 'Prob: 50% (TOUGH)'),
(259, 'Chicago', 23.8, 1026.3, 0, 19.4, NULL, '2026-02-22 06:00:00', 'Stable'),
(260, 'Chicago', 23.1, 1030.8, 0, 19.9, NULL, '2026-02-23 06:00:00', 'Stable'),
(261, 'Chicago', 41.8, 1029, 0, 3.6, 'E', '2026-04-11 03:44:43', 'Stable'),
(262, 'Chicago', 41.8, 1029, 0, 3.6, 'E', '2026-04-11 03:46:58', 'Stable'),
(263, 'Chicago', 41.8, 1029, 0, 3.6, 'NE', '2026-04-11 03:49:11', 'Stable'),
(264, 'Chicago', 46.5, 1009.1, 0.018, 31, NULL, '2026-03-22 05:00:00', 'Stable'),
(265, 'Chicago', 34.6, 1029, 0, 21.7, NULL, '2026-03-23 05:00:00', 'Cold Front'),
(266, 'Chicago', 39.7, 1028, 0, 13.7, NULL, '2026-03-24 05:00:00', 'Stable'),
(267, 'Chicago', 56.6, 1015.5, 0, 21.7, NULL, '2026-03-25 05:00:00', 'Stable'),
(268, 'Chicago', 38.4, 1029, 0, 0, 'NE', '2026-04-11 08:43:26', 'Stable'),
(269, 'Chicago', 38.4, 1029, 0, 0, 'NE', '2026-04-11 08:43:26', 'Stable'),
(270, 'Chicago', 53.2, 1028, 0, 5.8, 'E', '2026-04-11 19:36:06', 'Stable'),
(271, 'Chicago', 53.4, 1027, 0, 6.1, 'NE', '2026-04-11 20:44:01', 'Stable'),
(272, 'Chicago', 65.2, 1010, 0, 9.2, 'W', '2026-04-13 09:41:44', 'Stable');

-- --------------------------------------------------------

--
-- Table structure for table `blocks`
--

CREATE TABLE `blocks` (
  `blocker_username` varchar(255) NOT NULL,
  `blocked_username` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `catches` (
  `id` int(11) NOT NULL,
  `species` varchar(100) DEFAULT NULL,
  `time_caught` time DEFAULT NULL,
  `date_caught` date DEFAULT NULL,
  `weather_conditions` varchar(255) DEFAULT NULL,
  `lure_used` varchar(100) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `comments` (
  `id` int(11) NOT NULL,
  `post_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `parent_id` int(11) DEFAULT NULL,
  `content` text NOT NULL,
  `is_reported` tinyint(1) DEFAULT 0,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `fishing_spots` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `lat` decimal(10,8) NOT NULL,
  `lng` decimal(11,8) NOT NULL,
  `location_name` varchar(100) DEFAULT NULL,
  `species` varchar(50) DEFAULT NULL,
  `season` varchar(20) DEFAULT NULL,
  `time_of_day` varchar(20) DEFAULT NULL,
  `lure_used` varchar(100) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `gallery_posts` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `image_path` varchar(255) NOT NULL,
  `spot_name` varchar(100) DEFAULT NULL,
  `species` varchar(50) DEFAULT NULL,
  `lure_used` varchar(100) DEFAULT NULL,
  `season` varchar(20) DEFAULT NULL,
  `time_of_day` varchar(20) DEFAULT NULL,
  `is_reported` tinyint(1) DEFAULT 0,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `interactions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `target_id` int(11) NOT NULL,
  `target_type` enum('post','comment') NOT NULL,
  `vote` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `messages` (
  `id` int(11) NOT NULL,
  `sender_username` varchar(255) DEFAULT NULL,
  `receiver_username` varchar(255) DEFAULT NULL,
  `content` text DEFAULT NULL,
  `is_deleted` tinyint(1) DEFAULT 0,
  `timestamp` datetime DEFAULT current_timestamp(),
  `is_read` tinyint(1) DEFAULT 0,
  `msg_type` varchar(20) DEFAULT 'text'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `relationships` (
  `id` int(11) NOT NULL,
  `user_one` varchar(255) DEFAULT NULL,
  `user_two` varchar(255) DEFAULT NULL,
  `status` enum('friend','blocked') DEFAULT 'friend',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `reports` (
  `id` int(11) NOT NULL,
  `reporter_id` int(11) NOT NULL,
  `target_id` int(11) NOT NULL,
  `target_type` enum('post','comment') NOT NULL,
  `reason` varchar(255) DEFAULT NULL,
  `status` enum('pending','reviewed') DEFAULT 'pending'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `report_tickets` (
  `id` int(11) NOT NULL,
  `reporter_id` int(11) NOT NULL,
  `target_id` int(11) NOT NULL,
  `target_type` enum('post','comment') NOT NULL,
  `reason` varchar(255) DEFAULT NULL,
  `status` enum('pending','resolved') DEFAULT 'pending',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `social_relations` (
  `id` int(11) NOT NULL,
  `follower_id` int(11) NOT NULL,
  `followed_id` int(11) NOT NULL,
  `status` enum('following','friends') DEFAULT 'following',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `support_tickets` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `subject` varchar(255) NOT NULL,
  `category` enum('Technical','Billing','General','Feedback') DEFAULT 'General',
  `status` enum('Open','In Progress','Resolved','Closed') DEFAULT 'Open',
  `priority` enum('Low','Medium','High') DEFAULT 'Medium',
  `message` text NOT NULL,
  `admin_response` text DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `tickets` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `subject` varchar(255) DEFAULT NULL,
  `message` text DEFAULT NULL,
  `title` varchar(255) NOT NULL,
  `description` text NOT NULL,
  `status` enum('open','resolved') DEFAULT 'open',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `trips` (
  `id` int(11) NOT NULL,
  `location_name` varchar(255) DEFAULT NULL,
  `trip_success` int(11) DEFAULT NULL,
  `primary_species` varchar(100) DEFAULT NULL,
  `lures_used` varchar(255) DEFAULT NULL,
  `time_elapsed` varchar(50) DEFAULT NULL,
  `season` varchar(50) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `security_question` varchar(255) DEFAULT NULL,
  `security_answer` varchar(255) DEFAULT NULL,
  `mnemonic` varchar(255) DEFAULT NULL,
  `display_name` varchar(100) DEFAULT NULL,
  `profile_pic` varchar(255) DEFAULT NULL,
  `bio` varchar(500) DEFAULT NULL,
  `social_media` text DEFAULT NULL,
  `backup_email` varchar(100) DEFAULT NULL,
  `is_admin` tinyint(1) DEFAULT 0,
  `last_seen` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `weather_logs` (
  `id` int(11) NOT NULL,
  `log_date` date DEFAULT NULL,
  `pressure_low` float DEFAULT NULL,
  `pressure_high` float DEFAULT NULL,
  `wind_speed_low` float DEFAULT NULL,
  `wind_high` float DEFAULT NULL,
  `wind_dir` varchar(10) DEFAULT NULL,
  `temp_min` int(11) DEFAULT NULL,
  `temp_max` int(11) DEFAULT NULL,
  `trend_analysis` varchar(255) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

ALTER TABLE `api_weather_logs`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `blocks`
  ADD PRIMARY KEY (`blocker_username`,`blocked_username`);

ALTER TABLE `catches`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `comments`
  ADD PRIMARY KEY (`id`),
  ADD KEY `post_id` (`post_id`),
  ADD KEY `parent_id` (`parent_id`);

ALTER TABLE `fishing_spots`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `gallery_posts`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

ALTER TABLE `interactions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `unique_interaction` (`user_id`,`target_id`,`target_type`);

ALTER TABLE `messages`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `relationships`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `unique_rel` (`user_one`,`user_two`);

ALTER TABLE `reports`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `report_tickets`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `social_relations`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `unique_rel` (`follower_id`,`followed_id`);

ALTER TABLE `support_tickets`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

ALTER TABLE `tickets`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

ALTER TABLE `trips`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

ALTER TABLE `weather_logs`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `api_weather_logs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=273;

ALTER TABLE `catches`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

ALTER TABLE `comments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

ALTER TABLE `fishing_spots`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

ALTER TABLE `gallery_posts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

ALTER TABLE `interactions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

ALTER TABLE `messages`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

ALTER TABLE `relationships`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `reports`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `report_tickets`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

ALTER TABLE `social_relations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

ALTER TABLE `support_tickets`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

ALTER TABLE `tickets`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

ALTER TABLE `trips`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

ALTER TABLE `weather_logs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

ALTER TABLE `comments`
  ADD CONSTRAINT `comments_ibfk_1` FOREIGN KEY (`post_id`) REFERENCES `gallery_posts` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `comments_ibfk_2` FOREIGN KEY (`parent_id`) REFERENCES `comments` (`id`) ON DELETE CASCADE;

ALTER TABLE `gallery_posts`
  ADD CONSTRAINT `gallery_posts_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE;

ALTER TABLE `support_tickets`
  ADD CONSTRAINT `support_tickets_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE;

ALTER TABLE `tickets`
  ADD CONSTRAINT `tickets_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE;
COMMIT;

  ADD PRIMARY KEY (`id`);

ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

ALTER TABLE `weather_logs`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `api_weather_logs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=268;

ALTER TABLE `catches`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

ALTER TABLE `messages`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

ALTER TABLE `trips`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

ALTER TABLE `weather_logs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

CREATE TABLE IF NOT EXISTS fishing_spots (
    id INT AUTO_INCREMENT PRIMARY KEY,
    lat DECIMAL(10, 8) NOT NULL,
    lng DECIMAL(11, 8) NOT NULL,
    location_name VARCHAR(100),
    species VARCHAR(50),
    season VARCHAR(20),
    time_of_day VARCHAR(20),
    lure_used VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS gallery_posts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    image_path VARCHAR(255) NOT NULL,
    spot_name VARCHAR(100),
    species VARCHAR(50),
    lure_used VARCHAR(100),
    season VARCHAR(20),
    time_of_day VARCHAR(20),
    is_reported BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS comments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    post_id INT NOT NULL,
    user_id INT NOT NULL,
    parent_id INT DEFAULT NULL, 
    content TEXT NOT NULL,
    is_reported BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS interactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    target_id INT NOT NULL,
    target_type ENUM('post', 'comment') NOT NULL,
    vote TINYINT NOT NULL, 
    UNIQUE KEY (user_id, target_id, target_type)
);

CREATE TABLE IF NOT EXISTS social_relations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    follower_id INT NOT NULL,
    followed_id INT NOT NULL,
    status ENUM('following', 'friends') DEFAULT 'following',
    UNIQUE KEY (follower_id, followed_id)
);

CREATE TABLE IF NOT EXISTS report_tickets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    reporter_id INT NOT NULL,
    target_id INT NOT NULL,
    target_type ENUM('post', 'comment') NOT NULL,
    reason VARCHAR(255),
    status ENUM('pending', 'resolved') DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
