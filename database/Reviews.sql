-- phpMyAdmin SQL Dump
-- version 5.1.3-2.el7.remi
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: May 04, 2022 at 12:54 AM
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
-- Table structure for table `Reviews`
--

CREATE TABLE `Reviews` (
  `review_id` int(11) NOT NULL,
  `Games_game_id` int(11) NOT NULL,
  `Reviewers_reviewer_id` int(11) NOT NULL,
  `review_date` date NOT NULL,
  `rating` int(11) NOT NULL,
  `review_content` longtext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `Reviews`
--

INSERT INTO `Reviews` (`review_id`, `Games_game_id`, `Reviewers_reviewer_id`, `review_date`, `rating`, `review_content`) VALUES
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
-- Indexes for table `Reviews`
--
ALTER TABLE `Reviews`
  ADD PRIMARY KEY (`review_id`),
  ADD KEY `fk_Reviews_Reviewers1_idx` (`Reviewers_reviewer_id`),
  ADD KEY `fk_Reviews_Games1` (`Games_game_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Reviews`
--
ALTER TABLE `Reviews`
  MODIFY `review_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Reviews`
--
ALTER TABLE `Reviews`
  ADD CONSTRAINT `fk_Reviews_Games1` FOREIGN KEY (`Games_game_id`) REFERENCES `Games` (`game_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_Reviews_Reviewers1` FOREIGN KEY (`Reviewers_reviewer_id`) REFERENCES `Reviewers` (`reviewer_id`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
