%global tl_name knuth-lib
%global tl_revision 57963

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Core TeX and Metafont sources from Knuth
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/systems/knuth/dist/lib
License:	knuth
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/knuth-lib.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A collection of core TeX and Metafont macro files from DEK, apart from
the plain format and base. Includes the MF logo font(s), webmac.tex,
etc.

