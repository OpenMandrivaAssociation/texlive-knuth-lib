Name:		texlive-knuth-lib
Version:	20180303
Release:	1
Summary:	A small library of MetaFont sources
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/systems/knuth/dist/lib
License:	KNUTH
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/knuth-lib.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A collection of miscellaneous MetaFont source, including the
means to generate the logo font that is used for MetaFont and
MetaPost.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/knuth-lib
%{_texmfdistdir}/fonts/tfm/public/knuth-lib
%{_texmfdistdir}/tex/generic/knuth-lib
%{_texmfdistdir}/tex/plain/knuth-lib

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex %{buildroot}%{_texmfdistdir}
