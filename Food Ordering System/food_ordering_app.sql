-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Dec 22, 2020 at 09:44 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `food_ordering_app`
--

-- --------------------------------------------------------

--
-- Table structure for table `Customer_Info`
--

CREATE TABLE `Customer_Info` (
  `Cust_ID` int(11) NOT NULL,
  `Server_ID` int(11) NOT NULL,
  `Customer_Name` varchar(50) NOT NULL,
  `Food` varchar(100) NOT NULL,
  `Price` int(11) NOT NULL,
  `Quantity` int(11) NOT NULL,
  `Total_Payment` int(11) NOT NULL,
  `Payment_Method` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Customer_Info`
--

INSERT INTO `Customer_Info` (`Cust_ID`, `Server_ID`, `Customer_Name`, `Food`, `Price`, `Quantity`, `Total_Payment`, `Payment_Method`) VALUES
(13, 1, 'sabbhya', 'Biryani ----------------------------250', 250, 2, 500, 'UPI'),
(14, 9, 'maya', 'Wraps ------------------------------70', 70, 3, 210, 'UPI');

-- --------------------------------------------------------

--
-- Table structure for table `server`
--

CREATE TABLE `server` (
  `Server_ID` int(11) NOT NULL,
  `Name` varchar(20) NOT NULL,
  `DOB` date NOT NULL,
  `Mobile_No.` bigint(20) NOT NULL,
  `City` varchar(30) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `Password` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `server`
--

INSERT INTO `server` (`Server_ID`, `Name`, `DOB`, `Mobile_No.`, `City`, `Email`, `Password`) VALUES
(1, 'Maya', '1998-05-02', 7483659687, 'Pune', 'maya@gmail.com', '1234'),
(3, 'titu', '1987-09-12', 9263847561, 'Delhi', 'titumama@gmail.com', '12345'),
(6, 'mayank', '1996-03-24', 9081930038, 'surat', 'mayank@gmail.com', 'mk240396'),
(7, 'meena ', '1967-03-13', 9925139400, 'surat', 'meena@gmail.com', 'anamika'),
(8, 'Anjani Kumar Rungta', '1959-05-22', 9879036563, 'surat', 'ar@gmail.com', 'meena'),
(9, 'sabbhya', '2008-03-07', 9876543210, 'vapi', 'sabbhya@gmail.com', '123');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Customer_Info`
--
ALTER TABLE `Customer_Info`
  ADD PRIMARY KEY (`Cust_ID`);

--
-- Indexes for table `server`
--
ALTER TABLE `server`
  ADD PRIMARY KEY (`Server_ID`),
  ADD UNIQUE KEY `Mobile No.` (`Mobile_No.`),
  ADD UNIQUE KEY `Email` (`Email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Customer_Info`
--
ALTER TABLE `Customer_Info`
  MODIFY `Cust_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `server`
--
ALTER TABLE `server`
  MODIFY `Server_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
