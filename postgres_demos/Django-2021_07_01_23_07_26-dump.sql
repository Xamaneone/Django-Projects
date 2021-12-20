--
-- PostgreSQL database dump
--

-- Dumped from database version 13.3
-- Dumped by pg_dump version 13.3

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
-- Name: cat; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cat (
    cat_id bigint NOT NULL,
    cat_age integer NOT NULL,
    cat_name character varying(20),
    owner_id integer NOT NULL
);


ALTER TABLE public.cat OWNER TO postgres;

--
-- Name: cat_cat_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.cat_cat_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cat_cat_id_seq OWNER TO postgres;

--
-- Name: cat_cat_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.cat_cat_id_seq OWNED BY public.cat.cat_id;


--
-- Name: cat_room; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cat_room (
    cat_room_id bigint NOT NULL,
    register_date date NOT NULL,
    unregister_date date NOT NULL,
    hotel_id integer NOT NULL,
    cat_id integer NOT NULL
);


ALTER TABLE public.cat_room OWNER TO postgres;

--
-- Name: cat_room_cat_room_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.cat_room ALTER COLUMN cat_room_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.cat_room_cat_room_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: dog; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dog (
    dog_id bigint NOT NULL,
    dog_name character varying(20) NOT NULL,
    dog_age integer NOT NULL,
    owner_id integer NOT NULL
);


ALTER TABLE public.dog OWNER TO postgres;

--
-- Name: dog_dog_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.dog_dog_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dog_dog_id_seq OWNER TO postgres;

--
-- Name: dog_dog_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.dog_dog_id_seq OWNED BY public.dog.dog_id;


--
-- Name: dog_room; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dog_room (
    dog_room_id bigint NOT NULL,
    register_date date NOT NULL,
    unregister_date date NOT NULL,
    hotel_id integer NOT NULL,
    dog_id integer NOT NULL
);


ALTER TABLE public.dog_room OWNER TO postgres;

--
-- Name: dog_room_dog_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.dog_room_dog_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dog_room_dog_id_seq OWNER TO postgres;

--
-- Name: dog_room_dog_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.dog_room_dog_id_seq OWNED BY public.dog_room.dog_id;


--
-- Name: dog_room_dog_room_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.dog_room_dog_room_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dog_room_dog_room_id_seq OWNER TO postgres;

--
-- Name: dog_room_dog_room_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.dog_room_dog_room_id_seq OWNED BY public.dog_room.dog_room_id;


--
-- Name: dog_room_hotel_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.dog_room_hotel_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dog_room_hotel_id_seq OWNER TO postgres;

--
-- Name: dog_room_hotel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.dog_room_hotel_id_seq OWNED BY public.dog_room.hotel_id;


--
-- Name: hotel; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.hotel (
    hotel_id bigint NOT NULL,
    hotel_name character varying(25),
    hotel_stars integer
);


ALTER TABLE public.hotel OWNER TO postgres;

--
-- Name: hotel_hotel_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.hotel ALTER COLUMN hotel_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.hotel_hotel_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: owner; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.owner (
    owner_id bigint NOT NULL,
    owner_name character varying(15) NOT NULL,
    owner_age integer
);


ALTER TABLE public.owner OWNER TO postgres;

--
-- Name: owner_owner_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.owner_owner_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.owner_owner_id_seq OWNER TO postgres;

--
-- Name: owner_owner_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.owner_owner_id_seq OWNED BY public.owner.owner_id;


--
-- Name: cat cat_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cat ALTER COLUMN cat_id SET DEFAULT nextval('public.cat_cat_id_seq'::regclass);


--
-- Name: dog dog_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dog ALTER COLUMN dog_id SET DEFAULT nextval('public.dog_dog_id_seq'::regclass);


--
-- Name: dog_room dog_room_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dog_room ALTER COLUMN dog_room_id SET DEFAULT nextval('public.dog_room_dog_room_id_seq'::regclass);


--
-- Name: dog_room hotel_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dog_room ALTER COLUMN hotel_id SET DEFAULT nextval('public.dog_room_hotel_id_seq'::regclass);


--
-- Name: dog_room dog_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dog_room ALTER COLUMN dog_id SET DEFAULT nextval('public.dog_room_dog_id_seq'::regclass);


--
-- Name: owner owner_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.owner ALTER COLUMN owner_id SET DEFAULT nextval('public.owner_owner_id_seq'::regclass);


--
-- Data for Name: cat; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.cat (cat_id, cat_age, cat_name, owner_id) FROM stdin;
2	7	Jessy	3
3	3	Bubbles	2
\.


--
-- Data for Name: cat_room; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.cat_room (cat_room_id, register_date, unregister_date, hotel_id, cat_id) FROM stdin;
2	2020-06-10	2020-06-15	2	2
3	2020-06-20	2020-06-23	3	3
\.


--
-- Data for Name: dog; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dog (dog_id, dog_name, dog_age, owner_id) FROM stdin;
2	Bully	3	3
3	Rousey	5	1
\.


--
-- Data for Name: dog_room; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dog_room (dog_room_id, register_date, unregister_date, hotel_id, dog_id) FROM stdin;
2	2020-06-10	2020-06-15	2	2
3	2020-06-20	2020-06-23	3	3
\.


--
-- Data for Name: hotel; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.hotel (hotel_id, hotel_name, hotel_stars) FROM stdin;
1	Hotel 1	3
2	Grand Pets Hotel	5
3	Pets Heaven	2
\.


--
-- Data for Name: owner; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.owner (owner_id, owner_name, owner_age) FROM stdin;
1	Peter	26
2	George	32
3	Amy	67
\.


--
-- Name: cat_cat_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.cat_cat_id_seq', 3, true);


--
-- Name: cat_room_cat_room_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.cat_room_cat_room_id_seq', 3, true);


--
-- Name: dog_dog_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.dog_dog_id_seq', 12, true);


--
-- Name: dog_room_dog_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.dog_room_dog_id_seq', 1, false);


--
-- Name: dog_room_dog_room_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.dog_room_dog_room_id_seq', 3, true);


--
-- Name: dog_room_hotel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.dog_room_hotel_id_seq', 1, false);


--
-- Name: hotel_hotel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.hotel_hotel_id_seq', 3, true);


--
-- Name: owner_owner_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.owner_owner_id_seq', 12, true);


--
-- Name: cat cat_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cat
    ADD CONSTRAINT cat_pk PRIMARY KEY (cat_id);


--
-- Name: cat_room cat_room_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cat_room
    ADD CONSTRAINT cat_room_pkey PRIMARY KEY (cat_room_id);


--
-- Name: dog dog_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dog
    ADD CONSTRAINT dog_pk PRIMARY KEY (dog_id);


--
-- Name: dog_room dog_room_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dog_room
    ADD CONSTRAINT dog_room_pk PRIMARY KEY (dog_id);


--
-- Name: hotel hotel_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.hotel
    ADD CONSTRAINT hotel_pkey PRIMARY KEY (hotel_id);


--
-- Name: owner owner_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.owner
    ADD CONSTRAINT owner_pk PRIMARY KEY (owner_id);


--
-- Name: cat cat_owner__fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cat
    ADD CONSTRAINT cat_owner__fk FOREIGN KEY (owner_id) REFERENCES public.owner(owner_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: cat_room cat_room_dog__fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cat_room
    ADD CONSTRAINT cat_room_dog__fk FOREIGN KEY (cat_id) REFERENCES public.cat(cat_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: cat_room cat_room_hotel__fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cat_room
    ADD CONSTRAINT cat_room_hotel__fk FOREIGN KEY (hotel_id) REFERENCES public.hotel(hotel_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: dog dog_person__fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dog
    ADD CONSTRAINT dog_person__fk FOREIGN KEY (owner_id) REFERENCES public.owner(owner_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: dog_room dog_room_dog__fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dog_room
    ADD CONSTRAINT dog_room_dog__fk FOREIGN KEY (dog_id) REFERENCES public.dog(dog_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: dog_room dog_room_hotel__fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dog_room
    ADD CONSTRAINT dog_room_hotel__fk FOREIGN KEY (hotel_id) REFERENCES public.hotel(hotel_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

