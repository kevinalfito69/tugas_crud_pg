--
-- PostgreSQL database dump
--

-- Dumped from database version 14.2
-- Dumped by pg_dump version 14.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: toko_sembako; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.toko_sembako (
    id integer NOT NULL,
    nama_barang character varying(255),
    harga_barang integer,
    kode_barang integer
);


ALTER TABLE public.toko_sembako OWNER TO postgres;

--
-- Name: toko_sembako_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.toko_sembako_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.toko_sembako_id_seq OWNER TO postgres;

--
-- Name: toko_sembako_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.toko_sembako_id_seq OWNED BY public.toko_sembako.id;


--
-- Name: toko_sembako id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.toko_sembako ALTER COLUMN id SET DEFAULT nextval('public.toko_sembako_id_seq'::regclass);


--
-- Name: toko_sembako toko_sembako_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.toko_sembako
    ADD CONSTRAINT toko_sembako_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

