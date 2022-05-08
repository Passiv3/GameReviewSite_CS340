-- phpMyAdmin SQL Dump
-- version 5.1.3-2.el7.remi
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: May 08, 2022 at 11:08 PM
-- Server version: 10.6.7-MariaDB-log
-- PHP Version: 7.4.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cs340_chundann`
--

-- --------------------------------------------------------

--
-- Table structure for table `Developers`
--

CREATE TABLE `Developers` (
  `developer_id` int(11) NOT NULL,
  `developer_name` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `Developers`
--

INSERT INTO `Developers` (`developer_id`, `developer_name`) VALUES
(1, 'Ghost Games'),
(2, 'Valve'),
(3, 'CAPCOM'),
(4, 'Kojima Production')
;

-- --------------------------------------------------------

--
-- Table structure for table `GameGenres`
--

CREATE TABLE `GameGenres` (
  `game_id` int(11) NOT NULL,
  `genre_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `GameGenres`
--

INSERT INTO `GameGenres` (`game_id`, `genre_id`) VALUES
(1, 1),
(2, 2),
(2, 3),
(3, 4),
(4, 4),
(4, 5),
(5, 4),
(5, 6);

-- --------------------------------------------------------

--
-- Table structure for table `Games`
--

CREATE TABLE `Games` (
  `game_id` int(11) NOT NULL,
  `developer_id` int(11) DEFAULT NULL,
  `game_name` varchar(45) NOT NULL,
  `release_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `Games`
--

INSERT INTO `Games` (`game_id`, `developer_id`, `game_name`, `release_date`) VALUES
(1, 1, 'Need for Speed Heat', '2019-11-08'),
(2, 2, 'Counter Strike: Global Offensive', '2019-11-08'),
(3, 3, 'Monster Hunter: World', '2018-09-08'),
(4, 3, 'Devil May Cry V', '2018-09-08'),
(5, 4, 'Death Stranding', '2019-11-08');

-- --------------------------------------------------------

--
-- Table structure for table `Genres`
--

CREATE TABLE `Genres` (
  `genre_id` int(11) NOT NULL,
  `game_genre` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `Genres`
--

INSERT INTO `Genres` (`genre_id`, `game_genre`) VALUES
(1, 'Racing'),
(2, 'FPS'),
(3, 'Shooter'),
(4, 'Adventure'),
(5, 'Hack-And-Slash'),
(6, 'Action');

-- --------------------------------------------------------

--
-- Table structure for table `Reviewers`
--

CREATE TABLE `Reviewers` (
  `reviewer_id` int(11) NOT NULL,
  `reviewer_name` varchar(45) NOT NULL,
  `number_of_review` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `Reviewers`
--

INSERT INTO `Reviewers` (`reviewer_id`, `reviewer_name`, `number_of_review`) VALUES
(1, 'Gamecritic', 2),
(2, 'IGN', 2),
(3, 'Gamespot', 2);

-- --------------------------------------------------------

--
-- Table structure for table `Reviews`
--

CREATE TABLE `Reviews` (
  `review_id` int(11) NOT NULL,
  `game_id` int(11) NOT NULL,
  `reviewer_id` int(11) NOT NULL,
  `review_date` date NOT NULL,
  `rating` int(11) NOT NULL,
  `review_content` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `Reviews`
--

INSERT INTO `Reviews` (`review_id`, `game_id`, `reviewer_id`, `review_date`, `rating`, `review_content`) VALUES
(1, 1, 1, '2020-10-14', 6, 'This game is gas'),
(2, 2, 1, '2017-12-11', 7, 'This game is pretty good, but the matchmaking is terrible'),
(3, 3, 2, '2019-08-19', 9, 'The music and gameplay is awesome, classic Monster Hunter gameplay'),
(4, 3, 3, '2019-10-25', 8, 'Excellent entry of Monster Hunter'),
(5, 4, 3, '2017-12-11', 8, 'Smokin Sexy Style! The action for the long awaited sequel was worth the wait!'),
(6, 5, 2, '2017-12-11', 7, 'Very interesting game by Hideo Kojima');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Developers`
--
ALTER TABLE `Developers`
  ADD PRIMARY KEY (`developer_id`),
  ADD UNIQUE KEY `developer_name_UNIQUE` (`developer_name`);

--
-- Indexes for table `GameGenres`
--
ALTER TABLE `GameGenres`
  ADD PRIMARY KEY (`game_id`,`genre_id`),
  ADD KEY `fk_GameGenres_Genres1_idx` (`genre_id`);

--
-- Indexes for table `Games`
--
ALTER TABLE `Games`
  ADD PRIMARY KEY (`game_id`),
  ADD KEY `fk_Games_Developers_idx` (`developer_id`);

--
-- Indexes for table `Genres`
--
ALTER TABLE `Genres`
  ADD PRIMARY KEY (`genre_id`);

--
-- Indexes for table `Reviewers`
--
ALTER TABLE `Reviewers`
  ADD PRIMARY KEY (`reviewer_id`);

--
-- Indexes for table `Reviews`
--
ALTER TABLE `Reviews`
  ADD PRIMARY KEY (`review_id`),
  ADD KEY `fk_Reviews_Reviewers1_idx` (`reviewer_id`),
  ADD KEY `fk_Reviews_Games1` (`game_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Developers`
--
ALTER TABLE `Developers`
  MODIFY `developer_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `Games`
--
ALTER TABLE `Games`
  MODIFY `game_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `Genres`
--
ALTER TABLE `Genres`
  MODIFY `genre_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `Reviewers`
--
ALTER TABLE `Reviewers`
  MODIFY `reviewer_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `Reviews`
--
ALTER TABLE `Reviews`
  MODIFY `review_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `GameGenres`
--
ALTER TABLE `GameGenres`
  ADD CONSTRAINT `fk_GameGenres_Games1` FOREIGN KEY (`game_id`) REFERENCES `Games` (`game_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_GameGenres_Genres1` FOREIGN KEY (`genre_id`) REFERENCES `Genres` (`genre_id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `Games`
--
ALTER TABLE `Games`
  ADD CONSTRAINT `fk_Games_Developers` FOREIGN KEY (`developer_id`) REFERENCES `Developers` (`developer_id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `Reviews`
--
ALTER TABLE `Reviews`
  ADD CONSTRAINT `fk_Reviews_Games1` FOREIGN KEY (`game_id`) REFERENCES `Games` (`game_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_Reviews_Reviewers1` FOREIGN KEY (`reviewer_id`) REFERENCES `Reviewers` (`reviewer_id`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
