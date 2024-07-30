-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 30-07-2024 a las 20:12:47
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `flask`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `correo` varchar(50) NOT NULL,
  `clave` varchar(256) NOT NULL,
  `foto` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `nombre`, `correo`, `clave`, `foto`) VALUES
(14, 'maria', 'maria@gmail.com', '$2b$12$Un0pMMXJW08C6Qks8fWnE.WxuYXbsivwhhF61j5HapY', 'static/uploads\\imagen  fondo.jpg'),
(18, 'alejandra', 'alejandramancipe63@gmail.com', '$2b$12$xJ.z015GfAZpRfKjlHQaM.AcKFqPN6ytzJ83Klm85js1YqQDRLVpO', 'static/uploads\\imagen  fondo.jpg'),
(19, 'jhonny', 'jhonny@com.co', '$2b$12$aGxQOoSf1pE7P0JLbvN0J.73pAzxA0a5iHQRhYs7vAsI/4/MWEmGq', 'static/uploads\\imagen  fondo.jpg'),
(20, 'diana', 'diana@gmail.com', '$2b$12$xrxh19WwVlNCR/sqve1SG.8wcAI9D3.L69QDFryQApQD0ddLtz0Vi', 'static/uploads\\imagen  fondo.jpg'),
(21, 'jun', 'june@gmail.com', '$2b$12$3Uz8Q/W0zO7mFBoPpuDfauwgW5cuCEx48TV153QYO98tmKGT3pQVO', 'static/uploads\\imagen  fondo.jpg');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
