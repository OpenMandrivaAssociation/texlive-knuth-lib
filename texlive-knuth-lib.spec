# revision 33039
# category Package
# catalog-ctan /systems/knuth/dist/lib
# catalog-date 2014-02-16 23:23:15 +0100
# catalog-license knuth
# catalog-version undef
Name:		texlive-knuth-lib
Version:	20140216
Release:	4
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
%{_texmfdistdir}/fonts/source/public/knuth-lib/grayf.mf
%{_texmfdistdir}/fonts/source/public/knuth-lib/manfnt.mf
%{_texmfdistdir}/fonts/source/public/knuth-lib/slant.mf
%{_texmfdistdir}/fonts/tfm/public/knuth-lib/manfnt.tfm
%{_texmfdistdir}/tex/generic/knuth-lib/null.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex %{buildroot}%{_texmfdistdir}
