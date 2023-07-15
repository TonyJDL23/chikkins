PGDMP                         {            Restaurant_Chikkins    15.3    15.3     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                        0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    24578    Restaurant_Chikkins    DATABASE     �   CREATE DATABASE "Restaurant_Chikkins" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Spain.1252';
 %   DROP DATABASE "Restaurant_Chikkins";
             	   TonyJDL23    false                       0    0    DATABASE "Restaurant_Chikkins"    COMMENT     U   COMMENT ON DATABASE "Restaurant_Chikkins" IS 'Restaurante de hamburguesas CHIKKINS';
                	   TonyJDL23    false    3330            �            1259    24642    cliente    TABLE     �   CREATE TABLE public.cliente (
    cedula integer NOT NULL,
    nombre character varying(30),
    whatsapp character varying(13),
    email character varying(50)
);
    DROP TABLE public.cliente;
       public         heap    postgres    false            �            1259    24647    pedido    TABLE     �  CREATE TABLE public.pedido (
    num_pedido integer NOT NULL,
    cant_hambur integer,
    monto_delivery numeric(2,2),
    total_pagar numeric(3,2),
    modo_pago character varying(10),
    sreen_pago bytea,
    status character varying(12),
    fecha_hora timestamp without time zone,
    ciudad character varying(15),
    municipio character varying(15),
    observacion text,
    ced_cliente integer NOT NULL
);
    DROP TABLE public.pedido;
       public         heap    postgres    false            �          0    24642    cliente 
   TABLE DATA           B   COPY public.cliente (cedula, nombre, whatsapp, email) FROM stdin;
    public          postgres    false    214   �       �          0    24647    pedido 
   TABLE DATA           �   COPY public.pedido (num_pedido, cant_hambur, monto_delivery, total_pagar, modo_pago, sreen_pago, status, fecha_hora, ciudad, municipio, observacion, ced_cliente) FROM stdin;
    public          postgres    false    215          i           2606    24646    cliente cliente_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.cliente
    ADD CONSTRAINT cliente_pkey PRIMARY KEY (cedula);
 >   ALTER TABLE ONLY public.cliente DROP CONSTRAINT cliente_pkey;
       public            postgres    false    214            k           2606    24653    pedido pedido_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.pedido
    ADD CONSTRAINT pedido_pkey PRIMARY KEY (num_pedido);
 <   ALTER TABLE ONLY public.pedido DROP CONSTRAINT pedido_pkey;
       public            postgres    false    215            l           2606    24654    pedido pedido_ced_cliente_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.pedido
    ADD CONSTRAINT pedido_ced_cliente_fkey FOREIGN KEY (ced_cliente) REFERENCES public.cliente(cedula);
 H   ALTER TABLE ONLY public.pedido DROP CONSTRAINT pedido_ced_cliente_fkey;
       public          postgres    false    215    3177    214            �   9   x�32��4772�L�+�ϫ�442615���s3s���s�� ��TgDH]� �$s      �      x������ � �     