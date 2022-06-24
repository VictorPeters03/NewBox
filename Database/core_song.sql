-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Gegenereerd op: 24 jun 2022 om 16:22
-- Serverversie: 10.4.17-MariaDB
-- PHP-versie: 8.0.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `djangosearchbartest`
--

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `core_song`
--

CREATE TABLE `core_song` (
  `id` bigint(20) NOT NULL,
  `artist` varchar(50) NOT NULL,
  `song` varchar(100) NOT NULL,
  `uri` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Gegevens worden geëxporteerd voor tabel `core_song`
--

INSERT INTO `core_song` (`id`, `artist`, `song`, `uri`) VALUES
(1, 'Pantera', 'Cowboys from Hell', 'Pantera - Cowboys from Hell.mp3'),
(2, 'Primus', 'Jerry Was A Racecar Driver', 'Primus - Jerry Was a Race Car Driver.mp3'),
(6, 'Black Sabbath', 'Into the Void', 'BLACK SABBATH - Into the void.mp3'),
(8, 'Rick Astley', 'Never Gonna Give You Up', 'Rick Astley - Never Gonna Give You Up.mp3'),
(9, 'Alestorm', 'Keelhauled', 'Keelhauled - Alestorm.mp3'),
(10, 'Sacred Reich', 'Surf Nicaragua', 'SACRED REICH - Surf Nicaragua.mp3'),
(11, 'Purple Disco Machine, Sophie and the Giants', 'In The Dark', 'Purple Disco Machine, Sophie and the Giants - In The Dark.mp3'),
(12, 'The Weeknd, Ariana Grande', 'Save Your Tears', 'The Weeknd, Ariana Grande - Save Your Tears (Remix) (Official Video).mp3'),
(13, 'Nelly Furtado', 'Maneater', 'Nelly Furtado - Maneater.mp3'),
(14, 'JoeyAK', 'In Die Life', 'JoeyAK - In Die Life.mp3'),
(15, 'Darude', 'Sandstorm', 'Darude - Sandstorm.mp3'),
(16, 'Henk Wijngaard', 'Ik moet nog wat jaren mee', 'Henk Wijngaard - Ik moet nog wat jaren mee.mp3'),
(17, 'Dennis Schouten, Jan Roos, Madoc', 'Vieze Media', 'Dennis Schouten Jan Roos - Vieze Media (ft. Madoc).mp3'),
(18, 'Lady Roos', 'Buurmans Duiven', 'Buurmans Duiven koeroekoeroe Lady Roos.mp3'),
(19, 'Anita Meyer', 'Why Tell Me Why', 'Anita Meyer - Why Tell Me Why.mp3'),
(20, 'Dr. Peacock, Partyraiser', 'Trip To Holland', 'Dr. Peacock Partyraiser - Trip To Holland (Official Video).mp3'),
(21, 'Topic, A7S', 'Breaking Me', 'Topic - Breaking Me ft. A7S.mp3'),
(22, 'Tommee Profitt, Jordan Smith', 'Mary Did You Know', 'Mary Did You Know (feat. Jordan Smith) - Tommee Profitt [OFFICIAL MUSIC VIDEO].mp3'),
(23, 'Lynyrd Skynyrd', 'Sweet Home Alabama', 'Lynyrd Skynyrd - Sweet Home Alabama.mp3'),
(24, 'Jomarijan', 'Sweater Weather', 'Jomarijan - Sweater Weather.mp3'),
(25, 'Anri', 'Remember Summer Days', 'Anri - Remember Summer Days (Timely Track 11).mp3'),
(26, 'A Tribe Called Quest', 'Check The Rime', 'A Tribe Called Quest - Check The Rhime.mp3'),
(27, 'D-Block, S-te-Fan, D-Sturb', 'Feel It', 'D-Block S-te-Fan and D-Sturb - Feel It.mp3'),
(28, 'Carl Orff', 'O Fortuna', 'Carl Orff - O Fortuna - Latin and English Lyrics.mp3'),
(29, 'Alexander Ramm, Philipp Kopachevsky, Tchaikovsky', 'Nocturne op.19 No.4 for cello and piano', 'Alexander Ramm Philipp Kopachevsky Tchaikovsky Nocturne op.19 No.4 for cello and piano.mp3'),
(30, 'The Magic Flute', 'Queen of the Night aria', 'Mozarts The Magic Flute - Queen of the Night aria (Diana Damrau, The Royal Opera).mp3'),
(31, 'Tove Lo', 'Talking Body', 'Tove Lo - Talking Body.mp3'),
(32, 'DAZZ', 'Masterpiece', 'DAZZ - Masterpiece.mp3'),
(33, 'Swedish House Mafia', 'One (Your name)', 'Swedish House Mafia - One (Your Name).mp3'),
(34, 'Cosmo Sheldrake', 'Come Along', 'Cosmo Sheldrake - Come Along.mp3'),
(35, 'Cosmo Sheldrake', 'Solar Waltz', 'Cosmo Sheldrake - Solar Waltz.mp3'),
(36, 'Jack Stauber', 'The Ballad Of Hamantha', 'Jack Stauber - The Ballad Of Hamantha.mp3'),
(37, 'Fit For An Autopsy', 'No Man Is Without Fear', 'Fit For An Autopsy - No Man Is Without Fear Playthrough (Patrick Sheridan).mp3'),
(38, 'Wim Sonneveld', 'Het Dorp', 'Het Dorp - Wim Sonneveld (in HD).mp3'),
(39, 'Stiff Little Fingers', 'Alternative Ulster', 'Stiff Little Fingers - Alternative Ulster.mp3'),
(40, 'METRIC', 'Speed the Collapse', 'METRIC - Speed the Collapse (Official Lyric Video).mp3'),
(41, 'Eiffel 65', 'Blue (Da Ba Dee)', 'Eiffel 65 - Blue (Da Ba Dee).mp3'),
(42, 'Possessed', 'The Exorcist', 'Possessed - The Exorcist.mp3'),
(43, 'Deicide', 'Deicide', 'Deicide - Deicide.mp3'),
(44, 'Deicide', 'Dead by Dawn', 'Deicide - Dead by Dawn.mp3'),
(45, 'Horn', 'Verzet', 'Horn - Verzet.mp3'),
(46, 'Possessed', 'The Eyes of Horror', 'Possessed - The Eyes of Horror.mp3'),
(47, 'Lich King', 'Combat Mosh', 'LICH KING - Combat Mosh.mp3'),
(48, 'Exodus', 'The Toxic Waltz', 'Exodus - The Toxic Waltz.mp3'),
(49, 'NF', 'When I Grow Up', 'NF - When I Grow Up.mp3'),
(50, 'D-Block, S-te-Fan', 'Angels & Demons', 'D-Block, S-te-Fan - Angels Demons.mp3'),
(51, 'Headhunterz, Sub Zero Project', 'Our Church', 'Headhunterz Sub Zero Project - Our Church.mp3'),
(52, 'Headhunterz, Mike Taylor', 'Lift Me Up', 'Headhunterz - Lift Me Up feat. Mike Taylor.mp3'),
(53, 'Headhunterz, Conro, Clara Mae', 'Unique', 'Headhunterz Conro - Unique feat. Clara Mae.mp3'),
(54, 'LNY TNZ, Ruthless, The Kemist', 'We Don\'t Care', 'LNY TNZ Ruthless - We Dont Care (Ft. The Kemist).mp3');

--
-- Indexen voor geëxporteerde tabellen
--

--
-- Indexen voor tabel `core_song`
--
ALTER TABLE `core_song`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT voor geëxporteerde tabellen
--

--
-- AUTO_INCREMENT voor een tabel `core_song`
--
ALTER TABLE `core_song`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=55;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
